# Setting up this folder as a Claude project

## What already works, right now
This repo is a complete Claude Code project. Open a terminal in the repo root and run
`claude`, and you automatically get:

- **`CLAUDE.md` at the root and in `vapi-network/`** — loaded into every session, so the
  voice rules, the "only Call is live" rule and the no-invented-metrics rule apply
  without anyone re-explaining them.
- **8 slash commands** in `.claude/commands/` — `/weekly-content`, `/post-draft`,
  `/engage`, `/podcast-prep`, `/podcast-repurpose`, `/design-brief`, `/report`,
  `/research`. One per recurring job. This is the "different chats for different tasks"
  structure: a fresh session per job, started with its command.
- **Automatic logging** via `.claude/settings.json` → every prompt lands in
  `vapi-network/logs/prompts/YYYY-MM.md`, and every session transcript (raw + readable)
  lands in `vapi-network/logs/transcripts/`. Both hooks are tested and working.

```bash
cd <repo root>
claude
/weekly-content      # for example
```

## Linking it to a Project on claude.ai

A **Project** on claude.ai is created in the web/desktop UI — it can't be created from
here. Two ways to connect it to this folder:

**Option A — Claude Desktop with local folder access (closest to what you described).**
Create a Project in Claude Desktop, then add this repo as a local directory the project
can read. The Project then sees the same files, and chats inside it share this folder's
context. Each task gets its own chat inside that Project, which is exactly the
structure in `chat-map.md`.

**Option B — Push to GitHub and connect the repo.** This branch is
`claude/vapi-linkedin-podcast-setup-cc75a4` on `vankrimpen1994-creator/lottetest`.
Create a Project on claude.ai and connect the GitHub repo to it. Everything here becomes
Project knowledge, and it stays in sync as the repo updates.

**Project custom instructions** — paste in the contents of `vapi-network/CLAUDE.md`.
That gives web chats the same rules Claude Code sessions already get automatically.

> **Note on logging:** the automatic prompt/transcript capture is a **Claude Code**
> feature (it runs via hooks). Chats held in a claude.ai Project are stored by
> claude.ai but won't be written into `logs/` automatically. If everything must be
> captured in this folder, run the recurring work through Claude Code and use the
> Project for ad-hoc conversation.

## Weekly use
See `05-ops/chat-map.md` for which command to run on which day, and
`05-ops/weekly-workflow.md` for the full rhythm.
