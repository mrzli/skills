#!/usr/bin/env bash
set -euo pipefail

repo_root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)
skills_root=$repo_root/skills
codex_dir=$repo_root/.agents/skills
claude_dir=$repo_root/.claude/skills

if (($#)); then
  printf 'Usage: scripts/sync-skills.sh\n' >&2
  exit 2
fi

declare -A desired=()
for category in "$skills_root"/*; do
  [[ -d $category && ! -L $category ]] || continue
  [[ ${category##*/} == experimental ]] && continue
  for skill in "$category"/*; do
    [[ -d $skill && ! -L $skill && -f $skill/SKILL.md ]] || continue
    name=${skill##*/}
    if [[ -v desired[$name] ]]; then
      printf 'Duplicate skill name: %s\n' "$name" >&2
      exit 1
    fi
    desired[$name]=../../skills/${category##*/}/$name
  done
done

sync_dir() {
  local destination=$1 link name target
  mkdir -p -- "$destination"

  # Remove only stale links into this repository. Other skills are left alone.
  for link in "$destination"/*; do
    [[ -L $link ]] || continue
    target=$(readlink -- "$link")
    [[ $target == ../../skills/* || $target == "$skills_root/"* ]] || continue
    name=${link##*/}
    if [[ $target != "${desired[$name]-}" ]]; then
      rm -- "$link"
      printf 'Removed %s\n' "$link"
    fi
  done

  for name in "${!desired[@]}"; do
    link=$destination/$name
    if [[ -L $link ]]; then
      target=$(readlink -- "$link")
      [[ $target == "${desired[$name]}" ]] && continue
      rm -- "$link"
    elif [[ -e $link ]]; then
      printf 'Cannot replace non-symlink: %s\n' "$link" >&2
      return 1
    fi
    ln -s -- "${desired[$name]}" "$link"
    printf 'Linked %s -> %s\n' "$link" "${desired[$name]}"
  done
}

sync_dir "$codex_dir"
sync_dir "$claude_dir"
