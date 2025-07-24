#!/bin/bash
set -euo pipefail

#
# Copyright (c) 2025. Mohammed Alshehri <https://www.dralshehri.com>
#

# Script: release.sh
#
# Description:
# Automates Python package releases by updating version, changelog, and citation files,
# then commits changes and creates a git tag. Designed for projects using uv.
#
# Usage: bash release.sh <major|minor|patch>
#
# Prerequisites:
# - Run from project root on 'main' branch
# - All changes committed and synced with remote
# - CHANGELOG.md has '## Unreleased' section

handle_error() {
  echo -e "\033[31merror:\033[0m $1" >&2
  exit 1
}

confirm_action() {
  local msg="$1"
  echo -n "${msg} [N/y]: "
  read -r confirm
  [[ $confirm =~ ^[Yy]$ ]]
}

# Validate arguments and environment
if [[ $# -ne 1 ]]; then
  handle_error "specify version bump value"
fi

if [[ ! "$1" =~ ^(major|minor|patch)$ ]]; then
  handle_error "invalid bump value '$1' ('major', 'minor', or 'patch')"
fi

if [[ ! -f pyproject.toml ]]; then
  handle_error "run script from project root (pyproject.toml not found)"
fi

if ! grep -q "## Unreleased" CHANGELOG.md; then
  handle_error "ensure '## Unreleased' section exists in CHANGELOG.md"
fi

# Check git state
branch=$(git rev-parse --abbrev-ref HEAD)
if [[ "$branch" != "main" ]]; then
  handle_error "switch to the 'main' branch before releasing"
fi

if [[ -n "$(git status --porcelain)" ]]; then
  handle_error "commit or stash your changes before releasing"
fi

if [[ -n "$(git diff main origin/main)" ]]; then
  handle_error "push or pull changes to sync with remote"
fi

# Update version and metadata files
uv_output=$(uv version --bump "$1" 2>&1)
if ! echo "$uv_output" | grep -q "=>"; then
  handle_error "failed to update version with uv: $uv_output"
fi

version=$(grep '^version' pyproject.toml | awk -F '"' '{print $2}')
date=$(date +%Y-%m-%d)
echo "updated to version $version"

if ! sed -i "" "s/^## Unreleased.*/## $version - $date/" CHANGELOG.md; then
  handle_error "could not update CHANGELOG.md"
fi

if ! sed -i "" -e "s/^version: .*/version: $version/" \
          -e "s/^date-released: .*/date-released: $date/" CITATION.cff; then
  handle_error "could not update CITATION.cff"
fi

# Commit and tag release
if confirm_action "commit release and create tag?"; then
  git add -u
  git commit -m "Release $version"
  git tag -a "v$version" -m "Release $version"
  echo "created release commit and tag"

  if confirm_action "push to remote repository?"; then
    git push --follow-tags
    echo "release pushed to remote"
  fi
fi
