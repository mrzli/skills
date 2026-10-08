#!/usr/bin/env bash
# Summarize skill use recorded in local Claude Code and Codex transcripts.
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage: skill-usage.sh [--since YYYY-MM-DD] [--exclude-cwd PATH]... SKILLS_ROOT

Lists every skill under SKILLS_ROOT (directories containing SKILL.md) with:
  invoked   sessions where the skill was invoked (slash command, $name, or Skill tool)
  read      sessions where an agent read the skill's SKILL.md without invoking it
  last      date of the most recent invocation or read
Transcripts: ~/.claude/projects and ~/.codex/sessions (override with
CLAUDE_TRANSCRIPTS and CODEX_TRANSCRIPTS). Matching is by skill name only.
EOF
  exit 2
}

since=
excludes=()
while (($#)); do
  case $1 in
    --since) since=${2:?}; shift 2 ;;
    --exclude-cwd) excludes+=("$(realpath -m -- "${2:?}")"); shift 2 ;;
    -h|--help) usage ;;
    -*) usage ;;
    *) break ;;
  esac
done
(($# == 1)) || usage
skills_root=$1
command -v jq >/dev/null || { printf 'jq is required\n' >&2; exit 1; }

mapfile -t skills < <(find "$skills_root" -name SKILL.md -not -path '*/experimental/*' -printf '%h\n' | xargs -rn1 basename | sort -u)
((${#skills[@]})) || { printf 'No skills found under %s\n' "$skills_root" >&2; exit 1; }

claude_dir=${CLAUDE_TRANSCRIPTS:-$HOME/.claude/projects}
codex_dir=${CODEX_TRANSCRIPTS:-$HOME/.codex/sessions}

# Emits "kind<TAB>skill<TAB>date<TAB>cwd" for each transcript line that uses a skill.
extract='
  def skill_paths: [scan("([A-Za-z0-9_.-]+)/SKILL\\.md")[0]];
  def text_of: if type == "string" then . elif type == "array" then map(.text? // "") | join("\n") else "" end;
  (.timestamp // "")[0:10] as $date
  | (.cwd // .payload.cwd // "") as $cwd
  | (
      # Claude Code: slash commands, Skill tool, other tool calls reading SKILL.md
      (select(.type == "user") | .message.content | text_of
        | scan("<command-name>/?([^<]+)</command-name>")[0] | ["invoked", ., $date, $cwd]),
      (select(.type == "assistant") | .message.content[]? | select(.type == "tool_use")
        | if .name == "Skill" then ["invoked", .input.skill, $date, $cwd]
          elif (.name | IN("Read", "Bash", "Grep")) then (.input | tostring | skill_paths[] | ["read", ., $date, $cwd])
          else empty end),
      # Codex: injected <skill> blocks for $name, tool calls reading SKILL.md
      (select(.type == "response_item" and .payload.type == "message" and .payload.role == "user")
        | .payload.content | text_of
        | scan("<skill>\\s*<name>([^<]+)</name>")[0] | ["invoked", ., $date, $cwd]),
      (select(.type == "response_item" and ((.payload.type // "") | test("call$")))
        | (.payload.input // .payload.arguments // "") | tostring | skill_paths[] | ["read", ., $date, $cwd])
    )
  | @tsv'

{
  find "$claude_dir" "$codex_dir" -name '*.jsonl' -print0 2>/dev/null |
    while IFS= read -r -d '' file; do
      session=${file##*/}
      # Codex records cwd once in session_meta; Claude records it on each line.
      session_cwd=$(jq -r 'select(.type == "session_meta") | .payload.cwd' "$file" 2>/dev/null | head -n1)
      jq -r "$extract" "$file" 2>/dev/null |
        awk -F'\t' -v OFS='\t' -v s="$session" -v c="$session_cwd" '{ if ($4 == "") $4 = c; print $1, $2, $3, $4, s }'
    done
} |
  awk -F'\t' -v OFS='\t' -v since="$since" -v excl="$(IFS=$'\n'; printf '%s' "${excludes[*]}")" \
    -v names="$(IFS=$'\n'; printf '%s' "${skills[*]}")" '
    BEGIN {
      n = split(names, list, "\n"); for (i = 1; i <= n; i++) known[list[i]] = 1
      m = split(excl, ex, "\n")
    }
    {
      kind = $1; skill = $2; date = $3; cwd = $4; session = $5
      sub(/^.*:/, "", skill)
      if (!(skill in known) || (since != "" && date < since)) next
      for (i = 1; i <= m; i++) if (ex[i] != "" && index(cwd, ex[i]) == 1) next
      key = skill SUBSEP session
      if (kind == "invoked") { if (!(key in inv)) { inv[key] = 1; invoked[skill]++ } }
      else if (!(key in rd)) { rd[key] = 1; reads[skill]++ }
      if (date > last[skill]) last[skill] = date
    }
    END {
      print "skill", "invoked", "read", "last"
      for (i = 1; i <= n; i++) {
        s = list[i]
        print s, invoked[s] + 0, reads[s] + 0, (s in last && last[s] != "" ? last[s] : "never")
      }
    }' |
  { IFS= read -r header; printf '%s\n' "$header"; sort -t$'\t' -k2,2n -k3,3n -k1,1; } |
  column -t -s$'\t'
