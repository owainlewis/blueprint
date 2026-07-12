#!/bin/bash
# Regenerate golden examples using Blueprint skills.
# Run from the repo root: ./examples/regenerate.sh

set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
FEATURE="rag-chatbot"
INPUT="$DIR/input.md"

echo "Use Blueprint in your agent of choice with prompts like:"
echo ""
echo "  Use the spec skill. Write a spec for $FEATURE from examples/input.md"
echo "  After reviewing the spec, use the plan skill. Create a plan for $FEATURE from docs/$FEATURE/spec.md"
echo ""
echo "Expected outputs:"
echo ""
echo "  docs/$FEATURE/spec.md"
echo "  docs/$FEATURE/plan.md"
echo ""
echo "Then copy the reviewed outputs:"
echo ""
echo "  cp docs/$FEATURE/spec.md examples/$FEATURE/"
echo "  cp docs/$FEATURE/plan.md examples/$FEATURE/"
echo ""
echo "Input used:"
echo "  $INPUT"
echo ""
echo "Review the diffs:"
echo "  git diff examples/"
