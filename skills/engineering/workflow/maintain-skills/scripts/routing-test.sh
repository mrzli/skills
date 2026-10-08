#!/usr/bin/env bash
# Check which skills a fresh agent loads for requests that do not name a skill.
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage: routing-test.sh [--agent claude|codex] [--budget USD] [--allow-api-key] CASES_FILE

CASES_FILE is tab-separated, one case per line, with "#" comments allowed:
  PROJECT_DIR<TAB>EXPECTED<TAB>REQUEST
EXPECTED is a skill name, several acceptable names separated by commas,
or "none" when no skill should load.

Each request runs once in a fresh, read-only, unsaved session in PROJECT_DIR.
Prints each case with the skills the agent invoked or read and a verdict:
  pass     an expected skill loaded (or nothing loaded for "none")
  missed   an expected skill did not load
  extra    a skill loaded when "none" was expected
  absent   no expected skill was available to the agent (Claude only)
Runs use the skills installed for the agent, not the copies in this repository.
Claude runs stop if ANTHROPIC_API_KEY is set, since it would bill the API
instead of the subscription, unless --allow-api-key is given.
Raw output is kept in a temporary directory, printed at the end.
EOF
  exit 2
}

agent=claude
budget=0.50
allow_api_key=false
while (($#)); do
  case $1 in
    --agent) agent=${2:?}; shift 2 ;;
    --budget) budget=${2:?}; shift 2 ;;
    --allow-api-key) allow_api_key=true; shift ;;
    -h|--help|-*) usage ;;
    *) break ;;
  esac
done
(($# == 1)) || usage
[[ $agent == claude || $agent == codex ]] || usage
cases=$1
command -v jq >/dev/null || { printf 'jq is required\n' >&2; exit 1; }
command -v "$agent" >/dev/null || { printf '%s is not installed\n' "$agent" >&2; exit 1; }

if [[ $agent == claude && -n ${ANTHROPIC_API_KEY:-} && $allow_api_key == false ]]; then
  printf 'ANTHROPIC_API_KEY is set, so runs would bill the API. Unset it or pass --allow-api-key.\n' >&2
  exit 1
fi

out_dir=$(mktemp -d "${TMPDIR:-/tmp}/routing-test.XXXXXX")

run_case() {
  local dir=$1 request=$2 log=$3
  if [[ $agent == claude ]]; then
    (cd "$dir" && claude -p "$request" --permission-mode plan --no-session-persistence \
      --output-format stream-json --verbose --max-budget-usd "$budget" </dev/null) >"$log" 2>&1 || true
  else
    codex exec -C "$dir" -s read-only --ephemeral --skip-git-repo-check --json "$request" \
      </dev/null >"$log" 2>&1 || true
  fi
}

# Skills named by Skill tool calls, injected <skill> blocks, or SKILL.md paths in tool input.
loaded_skills() {
  jq -R -r '
    fromjson? // empty
    | [
        (.. | objects | select(.type? == "tool_use" and .name? == "Skill") | .input.skill?),
        (tostring | scan("<skill>\\s*<name>([^<]+)</name>")[0]),
        (.. | objects | select(.type? == "tool_use" and .name? != "Skill") | .input | tostring
          | scan("([A-Za-z0-9_.-]+)/SKILL\\.md")[0]),
        (select(.type? | tostring | test("item")) | tostring | scan("([A-Za-z0-9_.-]+)/SKILL\\.md")[0])
      ]
    | .[] | select(. != null) | sub("^.*:"; "")' "$1" | sort -u | paste -sd, -
}

# Skills the session offered the agent, from Claude's init event. Empty for Codex.
available_skills() {
  jq -r 'select(.type? == "system" and .subtype? == "init") | .skills[]? | sub("^.*:"; "")' "$1" 2>/dev/null | sort -u | paste -sd, -
}

n=0
printf 'case\texpected\tloaded\tverdict\trequest\n' >"$out_dir/results.tsv"
while IFS=$'\t' read -r dir expected request || [[ -n ${dir:-} ]]; do
  [[ -z ${dir:-} || $dir == \#* ]] && continue
  dir=${dir/#\~/$HOME}
  n=$((n + 1))
  log=$out_dir/case-$n.jsonl
  printf 'Running case %d in %s\n' "$n" "$dir" >&2
  run_case "$dir" "$request" "$log"
  loaded=$(loaded_skills "$log")
  verdict=missed
  if [[ $expected == none ]]; then
    [[ -z $loaded ]] && verdict=pass || verdict=extra
  else
    IFS=, read -ra wanted <<<"$expected"
    available=$(available_skills "$log")
    if [[ -n $available ]]; then
      verdict=absent
      for skill in "${wanted[@]}"; do
        [[ ",$available," == *",$skill,"* ]] && verdict=missed
      done
    fi
    for skill in "${wanted[@]}"; do
      [[ ",$loaded," == *",$skill,"* ]] && verdict=pass
    done
  fi
  printf '%d\t%s\t%s\t%s\t%s\n' "$n" "$expected" "${loaded:--}" "$verdict" "${request:0:60}" >>"$out_dir/results.tsv"
done <"$cases"

column -t -s$'\t' "$out_dir/results.tsv"
printf '\nRaw output: %s\n' "$out_dir"
