#!/bin/bash
# Regenerate the golden design and plan examples.
# Run from the repo root: ./examples/regenerate.sh

set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
FEATURE="rag-chatbot"
INPUT="$DIR/input.md"

echo "Use Blueprint with prompts like:"
echo ""
echo "  Use the design skill for $FEATURE from examples/input.md"
echo "  After reviewing the design, use the plan skill for docs/$FEATURE/design.md and return the plan in chat"
echo ""
echo "Expected outputs:"
echo ""
echo "  docs/$FEATURE/design.md"
echo "  a plan in chat, or tracker tickets when requested"
echo ""
echo "Then copy the reviewed design and example plan into examples/$FEATURE/ and review the diff."
echo "Input: $INPUT"
