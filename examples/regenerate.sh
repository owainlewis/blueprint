#!/bin/bash
# Regenerate golden examples using Blueprint skills.
# Run from the repo root: ./examples/regenerate.sh
#
# Requires an interactive Claude Code session because the
# spec skill may ask clarifying questions before writing.

set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
FEATURE="rag-chatbot"

echo "Run this command in an interactive Claude Code session:"
echo ""
echo "  /blueprint:spec $FEATURE $(head -1 "$DIR/input.md")"
echo ""
echo "Then copy the output:"
echo ""
echo "  cp docs/$FEATURE/spec.md examples/$FEATURE/"
echo ""
echo "Review the diffs:"
echo "  git diff examples/"
