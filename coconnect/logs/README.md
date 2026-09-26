# Logs

Everything this project's Claude Code sessions do is captured here automatically.
**Don't edit these by hand.**

| Path | What | Written by |
|---|---|---|
| `prompts/YYYY-MM.md` | Every prompt submitted, timestamped, grouped by month | `.claude/hooks/log-prompt.sh` (UserPromptSubmit) |
| `transcripts/YYYY-MM-DD-<sid>.jsonl` | Raw complete session transcript | `.claude/hooks/export-transcript.py` (Stop / SessionEnd) |
| `transcripts/YYYY-MM-DD-<sid>.md` | Readable digest — prompts and responses | same |
| `sessions/` | Hand-written session notes, when a session is worth summarising | you |

The hooks log into whichever client folder is named in `.claude/active-client` (falls back to `vapi-network`). Switch it when you change client.

Both hooks are configured in `.claude/settings.json` at the repo root and are written
to fail silently — they can never block or slow a session.

## Checking it's running
```bash
ls -la coconnect/logs/prompts coconnect/logs/transcripts
```
If a month file exists and is growing, it's working. Transcripts are written when a
session ends, so the current session won't appear until it stops.

## A note on privacy
Transcripts contain the full text of everything discussed in a session. If client
credentials, contracts or personal data ever get pasted into a session, they land here
too. Keep this repo private, and scrub before sharing any log externally.
