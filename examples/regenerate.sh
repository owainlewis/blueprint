#!/bin/bash
# Regenerate golden examples using Blueprint skills.
# Run from the repo root: ./examples/regenerate.sh

set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
FEATURE="rag-chatbot"
PROMPT="$(awk 'NF && $1 != "#" { print; exit }' "$DIR/input.md")"

echo "Use Blueprint in your agent of choice with prompts like:"
echo ""
echo "  Write a design doc for $FEATURE from examples/input.md"
echo "  After reviewing the design, write a spec for $FEATURE from docs/$FEATURE/design.md and examples/input.md"
echo "  After reviewing the spec, create a plan for $FEATURE from docs/$FEATURE/spec.md"
echo ""
echo "Then copy the outputs:"
echo ""
echo "  cp docs/$FEATURE/design.md examples/$FEATURE/"
echo "  cp docs/$FEATURE/spec.md examples/$FEATURE/"
echo "  cp docs/$FEATURE/plan.md examples/$FEATURE/"
echo ""
echo "Review the diffs:"
echo "  git diff examples/"
