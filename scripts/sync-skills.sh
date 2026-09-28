#!/usr/bin/env bash
set -euo pipefail

repo_root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)
skills_root=$repo_root/skills
destinations=(
  "$repo_root/.agents/skills"
  "$repo_root/.claude/skills"
)

if (($#)); then
  printf 'Usage: scripts/sync-skills.sh\n' >&2
  exit 2
fi

if [[ ! -d $skills_root || -L $skills_root || ! -r $skills_root || ! -x $skills_root ]]; then
  printf 'Source must be a readable, searchable directory, not a symlink: %s\n' "$skills_root" >&2
  exit 1
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

validate_destination() {
  local destination=$1 path name
  # Check both components before mkdir or cleanup can follow a symlink.
  for path in "${destination%/*}" "$destination"; do
    if [[ -L $path || ( -e $path && ! -d $path ) ]]; then
      printf 'Destination must be a directory, not a symlink: %s\n' "$path" >&2
      return 1
    fi
  done
  for name in "${!desired[@]}"; do
    path=$destination/$name
    if [[ -e $path && ! -L $path ]]; then
      printf 'Cannot replace non-symlink: %s\n' "$path" >&2
      return 1
    fi
  done
}

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

# Validate every destination before changing any of them.
for destination in "${destinations[@]}"; do
  validate_destination "$destination"
done

for destination in "${destinations[@]}"; do
  sync_dir "$destination"
done
