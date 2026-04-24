#!/bin/bash
# Regenerate golden examples using Blueprint skills.
# Run from the repo root: ./examples/regenerate.sh

set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
FEATURE="rag-chatbot"
PROMPT="$(awk 'NF && $1 != "#" { print; exit }' "$DIR/input.md")"

echo "Use Blueprint in your agent of choice with prompts like:"
echo ""
echo "  Create a plan for $FEATURE: $PROMPT"
echo "  Write specs only for tasks whose plan says Spec: full or short"
echo ""
echo "Then copy the outputs:"
echo ""
echo "  cp docs/$FEATURE/spec.md examples/$FEATURE/"
echo "  cp docs/$FEATURE/plan.md examples/$FEATURE/"
echo ""
echo "Review the diffs:"
echo "  git diff examples/"
