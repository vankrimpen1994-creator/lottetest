#!/usr/bin/env bash
# UserPromptSubmit hook — appends every prompt to the project's monthly prompt log.
# Never blocks the session: all failures exit 0 silently.
set -uo pipefail

INPUT=$(cat)
ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
LOGDIR="$ROOT/vapi-network/logs/prompts"
mkdir -p "$LOGDIR" 2>/dev/null || exit 0

MONTH=$(date -u +%Y-%m)
FILE="$LOGDIR/$MONTH.md"
TS=$(date -u +"%Y-%m-%d %H:%M:%SZ")

SID=$(printf '%s' "$INPUT" | jq -r '.session_id // "unknown"' 2>/dev/null) || SID=unknown
PROMPT=$(printf '%s' "$INPUT" | jq -r '.prompt // ""' 2>/dev/null) || PROMPT=""
[ -z "$PROMPT" ] && exit 0

[ -f "$FILE" ] || printf '# Prompt log — %s\n\n_Appended automatically by `.claude/hooks/log-prompt.sh`._\n' "$MONTH" > "$FILE"

{
  printf '\n---\n\n### %s · session `%s`\n\n' "$TS" "${SID:0:12}"
  printf '%s\n' "$PROMPT" | sed 's/^/> /'
} >> "$FILE"

exit 0
