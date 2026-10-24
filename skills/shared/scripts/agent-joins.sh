#!/usr/bin/env bash
# Open forks of an agent session in terminal tabs and pass notes between them.
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage: agent-joins.sh spawn TOPIC < BRIEF
       agent-joins.sh spawn --full [TOPIC]
       agent-joins.sh yield < NOTE
       agent-joins.sh collect
       agent-joins.sh prune TREE...

spawn    Opens a fork of the current tab in a new herdr or tmux tab in the
         current directory. The tab and the fork are named after the parent:
         Claude, Claude-1, Claude-1-1, and so on. By default the fork is a new
         session that starts by reading the brief from standard input. With
         --full it is a copy of the current session, told to focus on TOPIC
         if one is given. Forks only discuss: they are told not to change
         files and start without the file-editing tools.
yield    Stores standard input as the current fork's note, replacing any
         earlier version.
collect  Prints the notes of forks below the current tab, at any depth, that
         are new or changed since this tab last collected, and records them as
         read. Deletes notes that every tab above their fork has read, and lists
         trees with no activity for 14 days.
prune    Deletes everything recorded for the named trees, each given by the
         name of its top tab.

State lives in <git common dir>/agent-joins/:
  forks.tsv       one line per tab: name, parent, session ID, topic, created,
                  note version, updated ("-" marks an empty field)
  briefs/NAME.md  the brief fork NAME started from
  notes/NAME.md   the latest note yielded by fork NAME
  read/NAME.tsv   the notes tab NAME has collected: fork name, version
A fork knows its name from AGENT_FORK_NAME. A top tab is found by its session ID.
EOF
  exit 2
}

die() {
  printf '%s\n' "$*" >&2
  exit 1
}

stale_days=14

(($#)) || usage
command=$1
shift

git_dir=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) ||
  die 'Not in a Git repository: notes are kept in the Git directory.'
state=$git_dir/agent-joins
forks_file=$state/forks.tsv
mkdir -p "$state/briefs" "$state/notes" "$state/read"
touch "$forks_file"
exec 9>"$state/lock"
flock 9

now=$(date -u +%Y-%m-%dT%H:%M:%SZ)
session_id=
[[ -n ${CLAUDECODE:-} ]] && session_id=${CLAUDE_CODE_SESSION_ID:-}

names=()
declare -A parent=() session=() topic=() created=() version=() updated=()
while IFS=$'\t' read -r n p s t c v u; do
  [[ -n $n ]] || continue
  names+=("$n")
  parent[$n]=$p session[$n]=$s topic[$n]=$t created[$n]=$c version[$n]=$v updated[$n]=$u
done <"$forks_file"

save() {
  local n
  for n in "${names[@]}"; do
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$n" "${parent[$n]}" "${session[$n]}" \
      "${topic[$n]}" "${created[$n]}" "${version[$n]}" "${updated[$n]}"
  done >"$forks_file.tmp"
  mv "$forks_file.tmp" "$forks_file"
}

add_tab() { # NAME PARENT SESSION TOPIC
  names+=("$1")
  parent[$1]=$2 session[$1]=$3 topic[$1]=$4 created[$1]=$now version[$1]=0 updated[$1]=-
}

# Sets `me` to the current tab's name, or to nothing if it is not recorded.
me=
if [[ -n ${AGENT_FORK_NAME:-} ]]; then
  [[ -v parent[$AGENT_FORK_NAME] ]] ||
    die "This tab's fork, $AGENT_FORK_NAME, is not recorded. Its tree may have been pruned."
  me=$AGENT_FORK_NAME
  [[ ${session[$me]} == - && -n $session_id ]] && session[$me]=$session_id
elif [[ -n $session_id ]]; then
  for n in "${names[@]}"; do
    [[ ${session[$n]} == "$session_id" && ${parent[$n]} == - ]] && me=$n && break
  done
fi

ancestors() { # NAME: prints the tabs above NAME, nearest first
  local n=$1
  while [[ ${parent[$n]} != - ]]; do
    n=${parent[$n]}
    printf '%s\n' "$n"
  done
}

root_of() {
  local n=$1
  while [[ ${parent[$n]} != - ]]; do n=${parent[$n]}; done
  printf '%s\n' "$n"
}

is_below() { # NAME TAB: whether NAME is a fork below TAB at any depth
  local n=$1
  while [[ ${parent[$n]} != - ]]; do
    n=${parent[$n]}
    [[ $n == "$2" ]] && return 0
  done
  return 1
}

read_version() { # TAB FORK: the version of FORK's note that TAB has read
  local file=$state/read/$1.tsv
  [[ -f $file ]] || { echo 0; return; }
  awk -F'\t' -v f="$2" '$1 == f { v = $2 } END { print v + 0 }' "$file"
}

shown_topic() {
  [[ ${topic[$1]} == - ]] && return
  printf ': %s' "${topic[$1]}"
}

cmd_spawn() {
  local full=false
  [[ ${1:-} == --full ]] && full=true && shift
  (($# <= 1)) || usage
  local new_topic=${1:--}
  new_topic=${new_topic//[$'\t\n']/ }
  [[ -n $new_topic ]] || new_topic=-
  local brief=
  if ! $full; then
    [[ $new_topic != - ]] || die 'A brief-based fork needs a topic.'
    brief=$(cat)
    [[ -n ${brief//[[:space:]]/} ]] || die 'The brief is empty: pass it on standard input.'
  fi

  local fork_command prompt
  [[ -n $session_id ]] ||
    die 'Unsupported agent: only Claude Code sessions can be spawned (CLAUDECODE and CLAUDE_CODE_SESSION_ID are not set).'
  [[ -n ${HERDR_SESSION:-} || -n ${TMUX:-} ]] ||
    die 'No supported terminal multiplexer: run inside herdr or tmux.'

  if [[ -z $me ]]; then
    local i=1
    me=Claude
    while [[ -v parent[$me] ]]; do
      i=$((i + 1))
      me=Claude$i
    done
    add_tab "$me" - "$session_id" -
  fi

  local n number highest=0
  for n in "${names[@]}"; do
    [[ ${parent[$n]} == "$me" ]] || continue
    number=${n##*-}
    ((number > highest)) && highest=$number
  done
  local child=$me-$((highest + 1))
  local discuss_only="Only discuss here: do not create, edit, or delete files, and do not commit. Reading is fine. Record each change the user explicitly approves, so yield can pass it up to be implemented in the top tab."
  # The tool list comes before -n, which ends it, so the prompt is not read as a tool.
  local no_edits='--disallowedTools Edit,Write,NotebookEdit'
  if $full; then
    prompt="This tab is $child, a fork of this conversation."
    [[ $new_topic != - ]] && prompt+=" Focus on: $new_topic."
    printf -v fork_command 'claude --resume %q --fork-session %s -n %q %q' \
      "$session_id" "$no_edits" "$child" "$prompt $discuss_only"
  else
    local brief_file=$state/briefs/$child.md
    {
      printf '# Brief for %s: %s\n\n' "$child" "$new_topic"
      printf 'Spawned from %s on %s.\n\n' "$me" "$now"
      printf '%s\n' "$brief"
    } >"$brief_file"
    prompt="You are $child, a fork of $me. Read the brief at $brief_file and work on its point with the user. Refer to the items of $me by the IDs the brief uses. $discuss_only"
    printf -v fork_command 'claude %s -n %q %q' "$no_edits" "$child" "$prompt"
  fi

  if [[ -n ${HERDR_SESSION:-} ]]; then
    local create=(herdr tab create --cwd "$PWD" --label "$child" --env "AGENT_FORK_NAME=$child" --focus)
    [[ -n ${HERDR_WORKSPACE_ID:-} ]] && create+=(--workspace "$HERDR_WORKSPACE_ID")
    local created_tab pane_id
    created_tab=$("${create[@]}")
    pane_id=$(jq -er '.result.root_pane.pane_id' <<<"$created_tab") ||
      die "herdr tab create returned no pane ID: $created_tab"
    herdr pane run "$pane_id" "$fork_command" >/dev/null
  else
    tmux new-window -c "$PWD" -n "$child" -e "AGENT_FORK_NAME=$child" "$fork_command"
  fi

  add_tab "$child" "$me" - "$new_topic"
  save
  printf 'Opened %s, a fork of %s%s.\n' "$child" "$me" "$(shown_topic "$child")"
}

cmd_yield() {
  (($# == 0)) || usage
  [[ -n $me && ${parent[$me]} != - ]] ||
    die 'This tab is not a fork opened by spawn (AGENT_FORK_NAME is not set).'
  local body
  body=$(cat)
  [[ -n ${body//[[:space:]]/} ]] || die 'The note is empty: pass it on standard input.'

  local v=$((version[$me] + 1)) note=$state/notes/$me.md
  {
    printf '# %s%s\n\n' "$me" "$(shown_topic "$me")"
    printf 'Fork session: %s. Parent: %s. Version %s, %s.\n\n' \
      "${session[$me]/#-/unknown}" "${parent[$me]}" "$v" "$now"
    printf '%s\n' "$body"
  } >"$note.tmp"
  mv "$note.tmp" "$note"
  version[$me]=$v updated[$me]=$now
  save
  printf 'Saved version %s of the note of %s at %s.\n' "$v" "$me" "$note"
  printf 'Tabs above it: %s.\n' "$(ancestors "$me" | paste -sd, - | sed 's/,/, /g')"
}

cmd_collect() {
  (($# == 0)) || usage
  if [[ -z $me ]]; then
    echo 'No forks are recorded for this tab.'
  else
    local -A seen=()
    local file=$state/read/$me.tsv fork v
    if [[ -f $file ]]; then
      while IFS=$'\t' read -r fork v; do seen[$fork]=$v; done <"$file"
    fi
    local count=0 n note via
    for n in "${names[@]}"; do
      note=$state/notes/$n.md
      is_below "$n" "$me" && [[ -f $note ]] || continue
      ((${seen[$n]:-0} < ${version[$n]})) || continue
      if ((${seen[$n]:-0} == 0)); then v=new; else v=changed; fi
      via=
      [[ ${parent[$n]} != "$me" ]] && via=", via $(ancestors "$n" | sed "/^$me\$/,\$d" | tac | paste -sd, - | sed 's/,/, /g')"
      printf '=== %s: %s note, version %s%s ===\n\n' "$n" "$v" "${version[$n]}" "$via"
      cat "$note"
      echo
      seen[$n]=${version[$n]}
      count=$((count + 1))
    done
    ((count)) || echo 'No new or changed notes.'
    for fork in "${!seen[@]}"; do
      printf '%s\t%s\n' "$fork" "${seen[$fork]}"
    done | sort >"$file.tmp"
    mv "$file.tmp" "$file"
    save
  fi

  # A note stays until every tab above its fork has read its latest version.
  local n a waiting
  for n in "${names[@]}"; do
    [[ -f $state/notes/$n.md ]] || continue
    waiting=()
    while IFS= read -r a; do
      (($(read_version "$a" "$n") >= ${version[$n]})) || waiting+=("$a")
    done < <(ancestors "$n")
    if ((${#waiting[@]} == 0)); then
      rm "$state/notes/$n.md"
      printf 'Deleted the note of %s: every tab above it has collected it.\n' "$n"
    elif [[ -n $me ]] && is_below "$n" "$me"; then
      printf 'Kept the note of %s: not yet collected by %s.\n' "$n" "$(printf '%s\n' "${waiting[@]}" | paste -sd, - | sed 's/,/, /g')"
    fi
  done

  # List trees with no activity for a while, for the user to prune.
  local -A last=()
  local r t stamp limit
  limit=$(($(date +%s) - stale_days * 86400))
  for n in "${names[@]}"; do
    r=$(root_of "$n")
    for stamp in "${created[$n]}" "${updated[$n]}"; do
      [[ $stamp == - ]] && continue
      t=$(date -d "$stamp" +%s)
      ((t > ${last[$r]:-0})) && last[$r]=$t
    done
    if [[ -f $state/read/$n.tsv ]]; then
      t=$(stat -c %Y "$state/read/$n.tsv")
      ((t > ${last[$r]:-0})) && last[$r]=$t
    fi
  done
  local tabs notes
  for r in "${!last[@]}"; do
    ((last[$r] < limit)) || continue
    tabs=0 notes=0
    for n in "${names[@]}"; do
      [[ $(root_of "$n") == "$r" ]] || continue
      tabs=$((tabs + 1))
      [[ -f $state/notes/$n.md ]] && notes=$((notes + 1))
    done
    printf 'Inactive since %s: the tree of %s (tabs: %s, notes left: %s). Delete it with: prune %s\n' \
      "$(date -d "@${last[$r]}" +%F)" "$r" "$tabs" "$notes" "$r"
  done
  return 0
}

cmd_prune() {
  (($#)) || usage
  local r n kept=()
  for r in "$@"; do
    [[ -v parent[$r] && ${parent[$r]} == - ]] || die "Not the top tab of a recorded tree: $r"
  done
  for n in "${names[@]}"; do
    r=$(root_of "$n")
    if [[ " $* " == *" $r "* ]]; then
      rm -f "$state/briefs/$n.md" "$state/notes/$n.md" "$state/read/$n.tsv"
    else
      kept+=("$n")
    fi
  done
  names=("${kept[@]}")
  save
  printf 'Deleted the tree of %s.\n' "$@"
}

case $command in
  spawn | yield | prune) "cmd_$command" "$@" ;;
  collect)
    # Save all state before printing, so a closed output cannot lose a reading list.
    output=$state/collect.$$.tmp
    cmd_collect "$@" >"$output"
    cat "$output"
    rm "$output"
    ;;
  *) usage ;;
esac
