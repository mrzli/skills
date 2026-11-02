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
project checks.
EOF
  exit 2
}

record_message=
remove_message=
trailers=()
while (($#)); do
  case $1 in
    --record-message) record_message=${2:?}; shift 2 ;;
    --remove-message) remove_message=${2:?}; shift 2 ;;
    --trailer) trailers+=(--trailer "${2:?}"); shift 2 ;;
    --) shift; break ;;
    -h|--help|-*) usage ;;
    *) break ;;
  esac
done
(($# == 1)) || usage
file=$1

fail() { printf '%s\n' "$*" >&2; exit 1; }

git rev-parse --is-inside-work-tree >/dev/null 2>&1 || fail "Not inside a Git work tree"
[[ -f $file ]] || fail "No such file: $file"
git check-ignore -q -- "$file" && fail "Ignored by Git, so it cannot be committed: $file"

name=$(basename -- "$file")
name=${name%.*}
name=$(sed -E 's/^[0-9]{4}-[0-9]{2}-[0-9]{2}[-_]?//; s/[-_]+/ /g; s/ ?\bqueue$//' <<<"$name")
[[ -n $name || ( -n $record_message && -n $remove_message ) ]] || fail "Cannot derive a queue name from $file; pass both messages"
: "${record_message:=Record the $name queue as finished}"
: "${remove_message:=Remove the finished $name queue}"

git add -- "$file"
if git diff --cached --quiet HEAD -- "$file" 2>/dev/null; then
  printf 'No changes to record in %s; skipping the first commit\n' "$file"
else
  git commit --quiet --only -m "$record_message" "${trailers[@]}" -- "$file"
  git log -1 --format='%h %s'
fi

git rm --quiet -- "$file"
git commit --quiet -m "$remove_message" "${trailers[@]}"
git log -1 --format='%h %s'
