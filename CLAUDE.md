# Repo conventions

This repo holds client social/content engagements. One top-level folder per client.
Read the client's own `CLAUDE.md` before doing any work inside its folder — it
overrides anything here.

## Non-negotiables
1. **Never invent metrics, quotes, case studies, testimonials, or client results.**
   If a number isn't in a file in this repo or from a cited source, it doesn't go in
   a deliverable. Write `[NEEDS DATA: ...]` instead.
2. **Never publish or send anything externally** (LinkedIn, email, DMs, scheduling
   tools) without explicit per-item approval. Drafting is always safe; publishing never is.
3. **Everything is logged.** Session work is appended to the client's `logs/` folder.
   See `.claude/hooks/`. Don't disable it.
4. **Draft in files, not in chat.** Any deliverable longer than a few lines gets written
   to the right folder so it survives the session.
5. Dates in filenames are ISO: `YYYY-MM-DD`.
