# Coconnect — project instructions

Read this before any work in this folder.

## Who the client is
**Coconnect** is a Web3 marketing and campaign agency, founded December 2025. Rik Wijk is a
co-founder. It sells two things:
- **Core packages**: large campaigns such as the Outcome campaign.
- **Hub**: a promotion hub, priced as stated at $1,000 plus 10% of the prize pool. Faster to close, with repeat purchases possible.

**What we're building:** Coconnect's own AI commercial OS. It runs outbound lead generation, enrichment,
CRM, outreach, reply and proposal drafting, and reporting. It follows the SOP in `reference/`.
**Terms:** 20% commission on deals the engine brings in, for as long as the arrangement runs.
Coconnect pays for the tool subscriptions.

## Hard rules
1. **No invented metrics, quotes, case studies or results.** The Outcome figures ($1M prize pool,
   "40M volume", five-star review) are Rik's verbal claims. They stay out of outreach copy until we
   have them in writing. Until then, write `[NEEDS DATA: ...]`.
2. **Nothing is sent, posted or DM'd externally without explicit per-item approval.** A robot never
   sends to a prospect. Drafts plus a Slack ping, always.
3. **The AI fills variables. It never writes the message.** Coconnect writes the templates.
4. **Nothing writes to the CRM before a human reviews the sheet.**
5. **Two motions, two pipelines.** Core packages and Hub have separate ICPs, sources, cadences and copy.
   Never mix them in one campaign.
6. **Don't contact anyone Coconnect already reaches another way.** Dedupe against the CRM, against Bull Shark's
   lists, and against warm and partner intros before anything goes out.
7. Follow the SOP's hard rules (`reference/Commercial-Sales-OS-SOP.md`), unless this file overrides them.

## Where things go
| | |
|---|---|
| `00-discovery/` | Call transcripts, notes, intake questionnaire and Coconnect's answers |
| `01-build-plan/` | The step-by-step build plan and the homework tracker |
| `reference/` | The SOP and the Playbook from the previous cohort (Appic build). Read-only. |
| `logs/` | Auto-captured prompts and transcripts. `sessions/` is for hand-written notes. |
