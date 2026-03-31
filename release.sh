#!/usr/bin/env bash
set -euo pipefail

# Usage: ./release.sh [major|minor|patch]
# Defaults to patch if no argument given.

BUMP="${1:-patch}"
PLUGIN=".claude-plugin/plugin.json"
MARKETPLACE=".claude-plugin/marketplace.json"

# Read current version from plugin.json
CURRENT=$(grep '"version"' "$PLUGIN" | head -1 | sed 's/[^0-9.]//g')

if [[ -z "$CURRENT" ]]; then
  echo "Error: could not read version from $PLUGIN"
  exit 1
fi

IFS='.' read -r MAJOR MINOR PATCH <<< "$CURRENT"

case "$BUMP" in
  major) MAJOR=$((MAJOR + 1)); MINOR=0; PATCH=0 ;;
  minor) MINOR=$((MINOR + 1)); PATCH=0 ;;
  patch) PATCH=$((PATCH + 1)) ;;
  *) echo "Usage: ./release.sh [major|minor|patch]"; exit 1 ;;
esac

NEW="${MAJOR}.${MINOR}.${PATCH}"

echo "Bumping version: ${CURRENT} → ${NEW}"

# Update all version fields in both files
sed -i '' "s/\"version\": \"${CURRENT}\"/\"version\": \"${NEW}\"/g" "$PLUGIN" "$MARKETPLACE"

# Commit and tag
git add "$PLUGIN" "$MARKETPLACE"
git commit -m "release: v${NEW}"
git tag "v${NEW}"
git push && git push --tags

echo "Released v${NEW}"
