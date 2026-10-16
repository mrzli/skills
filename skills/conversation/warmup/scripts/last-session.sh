#!/usr/bin/env bash
# Print the last messages of the most recent earlier agent session in a project.
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage: last-session.sh [--messages N] [--skip N] [PROJECT_DIR]

Finds Claude Code and Codex sessions whose working directory is PROJECT_DIR
(default: the current directory), newest first, and prints the user and
assistant text of the last N messages (default 30) of one of them. Tool calls
and their output are left out, and long messages are shortened.
--skip N passes over the N newest sessions (default 1, the current session).
Transcripts: ~/.claude/projects and ~/.codex/sessions (override with
CLAUDE_TRANSCRIPTS and CODEX_TRANSCRIPTS). Codex sessions are searched from
the last 30 days.
EOF
  exit 2
}

messages=30
skip=1
while (($#)); do
  case $1 in
    --messages) messages=${2:?}; shift 2 ;;
    --skip) skip=${2:?}; shift 2 ;;
    -h|--help|-*) usage ;;
    *) break ;;
  esac
done
(($# <= 1)) || usage
project=$(realpath -m -- "${1:-$PWD}")
command -v jq >/dev/null || { printf 'jq is required\n' >&2; exit 1; }

claude_dir=${CLAUDE_TRANSCRIPTS:-$HOME/.claude/projects}
codex_dir=${CODEX_TRANSCRIPTS:-$HOME/.codex/sessions}

# Emits "mtime<TAB>agent<TAB>file" for each session in the project.
sessions() {
  local slug=${project//[\/.]/-}
  find "$claude_dir/$slug" -maxdepth 1 -name '*.jsonl' -printf '%T@\tclaude\t%p\n' 2>/dev/null || true
  find "$codex_dir" -name '*.jsonl' -mtime -30 -printf '%T@\t%p\n' 2>/dev/null |
    while IFS=$'\t' read -r mtime file; do
      cwd=$(head -n1 "$file" | jq -r 'select(.type == "session_meta") | .payload.cwd // empty' 2>/dev/null)
      if [[ $cwd == "$project" ]]; then printf '%s\tcodex\t%s\n' "$mtime" "$file"; fi
    done
}

session=$(sessions | sort -rn | sed -n "$((skip + 1))p")
[[ -n $session ]] || { printf 'No earlier session found for %s\n' "$project" >&2; exit 1; }
IFS=$'\t' read -r mtime agent file <<<"$session"
printf 'Session: %s %s, last active %s\n\n' "$agent" "$file" "$(date -d "@${mtime%.*}" '+%Y-%m-%d %H:%M')"

if [[ $agent == claude ]]; then
  filter='
    select((.type == "user" or .type == "assistant") and (.isMeta // false) == false)
    | .type as $role
    | (.message.content | if type == "string" then . else map(select(.type == "text") | .text) | join("\n") end)
    | select(. != "" and (startswith("<local-command") | not))
    | [$role, .]'
else
  filter='
    select(.type == "response_item" and .payload.type == "message"
      and (.payload.role == "user" or .payload.role == "assistant"))
    | .payload.role as $role
    | (.payload.content | map(.text? // "") | join("\n"))
    | select(. != "" and (test("^\\s*(<environment_context>|<user_instructions>|<skill>|# AGENTS\\.md)") | not))
    | [$role, .]'
fi

jq -c "$filter" "$file" 2>/dev/null | tail -n "$messages" |
  jq -r '.[0] as $role | .[1] | (if length > 1500 then .[0:1500] + " […]" else . end) | "\($role | ascii_upcase):\n\(.)\n"'
