#!/usr/bin/env bash
set -euo pipefail

repo_root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)
skills_root=$repo_root/skills

# By default, link the skills into this repository's discovery directories.
# With --user, link them into the user's, for every project.
user=false
if (($# == 1)) && [[ $1 == --user ]]; then
  user=true
elif (($#)); then
  printf 'Usage: scripts/sync-skills.sh [--user]\n' >&2
  exit 2
fi

if [[ $user == true ]]; then
  : "${HOME:?HOME must be set}"
  destinations=("$HOME/.agents/skills" "$HOME/.claude/skills")
else
  destinations=("$repo_root/.agents/skills" "$repo_root/.claude/skills")
fi

if [[ ! -d $skills_root || -L $skills_root || ! -r $skills_root || ! -x $skills_root ]]; then
  printf 'Source must be a readable, searchable directory, not a symlink: %s\n' "$skills_root" >&2
  exit 1
fi

declare -A desired=()
discover_skills() {
  local directory=$1 child name
  if [[ ! -r $directory || ! -x $directory ]]; then
    printf 'Source directory must be readable and searchable: %s\n' "$directory" >&2
    exit 1
  fi
  for child in "$directory"/*; do
    [[ -d $child && ! -L $child ]] || continue
    [[ $child == "$skills_root/experimental" ]] && continue
    if [[ ! -f $child/SKILL.md ]]; then
      discover_skills "$child"
      continue
    fi
    name=${child##*/}
    if [[ -v desired[$name] ]]; then
      printf 'Duplicate skill name: %s\n' "$name" >&2
      exit 1
    fi
    # A skill's supporting directories are not separate skills.
    if [[ $user == true ]]; then
      desired[$name]=$child
    else
      desired[$name]=../../skills/${child#"$skills_root/"}
    fi
  done
}

discover_skills "$skills_root"

# A link is managed when it points into this repository's skills. Other links
# belong to the user or another installation and are left alone.
managed_link() {
  local target
  [[ -L $1 ]] || return 1
  target=$(readlink -- "$1")
  [[ $target == "$skills_root/"* ]] && return 0
  [[ $user == false && $target == ../../skills/* ]]
}

validate_destination() {
  local destination=$1 path name
  if [[ $user == true ]]; then
    # The user's directories may be symlinks, such as into a dotfiles checkout.
    if [[ -e $destination && ! -d $destination ]]; then
      printf 'Destination must be a directory: %s\n' "$destination" >&2
      return 1
    fi
  else
    # Check both components before mkdir or cleanup can follow a symlink.
    for path in "${destination%/*}" "$destination"; do
      if [[ -L $path || ( -e $path && ! -d $path ) ]]; then
        printf 'Destination must be a directory, not a symlink: %s\n' "$path" >&2
        return 1
      fi
    done
  fi
  for name in "${!desired[@]}"; do
    path=$destination/$name
    if [[ $user == true ]]; then
      if [[ -e $path || -L $path ]] && ! managed_link "$path"; then
        printf 'Cannot replace a skill this repository does not manage: %s\n' "$path" >&2
        if [[ ! -e $path ]]; then
          printf 'It is a broken link, such as from a moved clone. Remove broken links with\n' >&2
          { printf '  find -L'; printf ' %q' "${destinations[@]}"; printf ' -maxdepth 1 -type l -delete\n'; } >&2
          printf 'and run the script again.\n' >&2
        fi
        return 1
      fi
    elif [[ -e $path && ! -L $path ]]; then
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
    managed_link "$link" || continue
    target=$(readlink -- "$link")
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
