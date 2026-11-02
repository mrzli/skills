#!/usr/bin/env bash
# Commit a finished queue file in its final state, then delete it in a second commit.
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage: finish-queue.sh [--record-message MSG] [--remove-message MSG]
                       [--trailer TRAILER]... QUEUE_FILE

Commits QUEUE_FILE as it is in the working tree, and only that file, so the
finished queue stays in history. It skips this commit when the file has no
changes since its last commit. Then deletes the file and commits the deletion
together with everything else already staged, such as a closed backlog item.

Messages derived from the file name, here for .scratch/delivery/2026-11-02-app-architecture.md:
  Record the app architecture queue as finished
  Remove the finished app architecture queue
--record-message and --remove-message replace them. --trailer adds a trailer,
such as "Co-Authored-By: Name <email>", to both commits. The script runs no
project checks. Each commit is printed with the files it changed.

If the removal commit fails, such as when a hook rejects it, the deletion stays
staged. Fix the cause and rerun the same command to make only that commit.
EOF
  exit "${1:-2}"
}

value() { [[ $# -ge 2 && -n $2 ]] || usage; }

record_message=
remove_message=
trailers=()
while (($#)); do
  case $1 in
    --record-message) value "$@"; record_message=$2; shift 2 ;;
    --remove-message) value "$@"; remove_message=$2; shift 2 ;;
    --trailer) value "$@"; trailers+=(--trailer "$2"); shift 2 ;;
    --) shift; break ;;
    -h|--help) usage 0 ;;
    -*) usage ;;
    *) break ;;
  esac
done
(($# == 1)) || usage
file=$1

fail() { printf '%s\n' "$*" >&2; exit 1; }

git rev-parse --is-inside-work-tree >/dev/null 2>&1 || fail "Not inside a Git work tree"
# A staged deletion of a missing file means an earlier removal commit failed.
resume=false
if [[ ! -e $file && -n $(git diff --cached --name-only --diff-filter=D -- "$file") ]]; then
  resume=true
else
  [[ -f $file ]] || fail "No such file: $file"
  git check-ignore -q -- "$file" && fail "Ignored by Git, so it cannot be committed: $file"
fi

name=$(basename -- "$file")
name=${name%.*}
name=$(sed -E 's/^[0-9]{4}-[0-9]{2}-[0-9]{2}[-_]?//; s/[-_]+/ /g; s/(^| )queue$//' <<<"$name")
[[ -n $name || ( -n $record_message && -n $remove_message ) ]] || fail "Cannot derive a queue name from $file; pass both messages"
: "${record_message:=Record the $name queue as finished}"
: "${remove_message:=Remove the finished $name queue}"

show() { git log -1 --format='%h %s' --stat; }

if $resume; then
  printf 'Deletion of %s already staged; making only the removal commit\n' "$file"
else
  git add -- "$file"
  if git diff --cached --quiet HEAD -- "$file" 2>/dev/null; then
    printf 'No changes to record in %s; skipping the first commit\n' "$file"
  else
    git commit --quiet --only -m "$record_message" "${trailers[@]}" -- "$file"
    show
  fi
  git rm --quiet -- "$file"
fi

git commit --quiet -m "$remove_message" "${trailers[@]}"
show
