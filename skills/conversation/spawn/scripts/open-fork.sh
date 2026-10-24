#!/usr/bin/env bash
# Open a fork of the current agent session in a new terminal tab.
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage: open-fork.sh TOPIC

Opens a new herdr or tmux tab in the current directory, labeled TOPIC, that
starts a fork of the current Claude Code session named TOPIC. The new tab gets
AGENT_PARENT_SESSION set to the current session's ID.
EOF
  exit 2
}

(($# == 1)) && [[ -n $1 && $1 != -* ]] || usage
topic=$1

if [[ -n ${CLAUDECODE:-} && -n ${CLAUDE_CODE_SESSION_ID:-} ]]; then
  session_id=$CLAUDE_CODE_SESSION_ID
  printf -v fork_command 'claude --resume %q --fork-session -n %q' "$session_id" "$topic"
else
  printf 'Unsupported agent: only Claude Code sessions can be forked (CLAUDECODE and CLAUDE_CODE_SESSION_ID are not set).\n' >&2
  exit 1
fi

if [[ -n ${HERDR_SESSION:-} ]]; then
  create=(herdr tab create --cwd "$PWD" --label "$topic" --env "AGENT_PARENT_SESSION=$session_id" --focus)
  [[ -n ${HERDR_WORKSPACE_ID:-} ]] && create+=(--workspace "$HERDR_WORKSPACE_ID")
  created=$("${create[@]}")
  pane_id=$(jq -er '.result.root_pane.pane_id' <<<"$created") || {
    printf 'herdr tab create returned no pane ID: %s\n' "$created" >&2
    exit 1
  }
  herdr pane run "$pane_id" "$fork_command" >/dev/null
  printf 'Opened herdr tab "%s" (pane %s): %s\n' "$topic" "$pane_id" "$fork_command"
elif [[ -n ${TMUX:-} ]]; then
  tmux new-window -c "$PWD" -n "$topic" -e "AGENT_PARENT_SESSION=$session_id" "$fork_command"
  printf 'Opened tmux window "%s": %s\n' "$topic" "$fork_command"
else
  printf 'No supported terminal multiplexer: run inside herdr or tmux.\n' >&2
  exit 1
fi
