# Session 01 — Project setup & pitch preparation
**Date:** 2026-09-20 · **Goal:** stand up the project folder and prepare tomorrow's agency pitch

> **Superseded in part — see `2026-09-21-session-02-corrections.md`.** This session led
> with the x402/Call plumbing rather than the hiring-and-escrow proposition, and prepared
> for a client meeting rather than an agency one. Both corrected the next day.

## What was asked
Build a dedicated project folder for the vAPI Network trial (LinkedIn from scratch,
podcast management, graphic design), structured so different tasks run in different
sessions, with full prompt/output logging — and prepare a 3-month plan to pitch in a
30-minute meeting tomorrow.

## Research findings (the two that changed the approach)

**1. vapinetwork.ai is not what the brief implied.** It's an **onchain task market for
agents and humans** — a non-custodial toolkit for discovering and paying x402 APIs.
Products: Call (live), Tasks, Compute, Stake (not live). Web3 × AI-agent infrastructure,
not a recruitment platform. "Recruitment to the platform" reads as **two-sided market
supply/demand acquisition**, and the whole content strategy is built on that split.

**2. There's a severe name collision.** `vapi.ai` — voice AI, YC W21, $50M Series B in
May 2026, 1M+ developers — owns every "VAPI" search on LinkedIn, where search is
name-match weighted. This is a real commercial problem with a free fix, and it became
the opening move of the pitch.

Supporting: x402 governance moved to the **Linux Foundation in April 2026** (Google, Visa,
Mastercard, Stripe, AWS, Circle). 69,000 active agents, 165M transactions. This is the
"it's a standard, not a crypto toy" ammunition that makes the category legible to a
LinkedIn B2B audience.

_Note: `vapinetwork.ai` itself is blocked by this environment's egress proxy. Findings
came from the GitHub repo, search results and ecosystem sources — all cited in
`01-strategy/client-profile.md`. **Verify the homepage copy directly before the meeting.**_

## What was built
- Full project folder: `00-pitch/` → `05-ops/`, plus `logs/`
- Pitch pack: 30-minute run-sheet, 90-day plan, scope & pricing, objection handling, discovery questions, 3 sample posts
- Strategy: client profile, ICP & positioning, content pillars, voice & tone, KPI framework with honest target bands
- Ops: weekly workflow, chat map, Week-0 checklist, reporting templates
- 8 slash commands in `.claude/commands/` — one per recurring job
- Automatic logging hooks (prompts + transcripts), both smoke-tested

## Open questions for the client call
Tracked in `00-pitch/discovery-questions.md`. The two that most affect scope:
- Is $1,300 monthly or for the whole 90 days?
- Will founders post from personal profiles? _(Determines whether the target bands are realistic.)_
