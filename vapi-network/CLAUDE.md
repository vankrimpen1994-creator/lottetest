# vAPI Network — project instructions

Read this before any work in this folder. Full research: `01-strategy/client-profile.md`.

## Who the client is (get this right — there's a name collision)
**vAPI Network** (`vapinetwork.ai`) — "onchain task market for agents and humans".
Non-custodial toolkit for discovering and paying x402 APIs. Products: **Call (live)**,
Tasks, Compute, Stake (not live).

**They are NOT `vapi.ai`**, the voice-AI company (YC W21, $50M Series B, 1M+ devs).
Different company. When researching, always disambiguate.

## Hard rules
1. **Only Call is live.** Never write copy implying Tasks, Compute or Stake have shipped.
   Pre-launch products get build-in-public framing only.
2. **Always "vAPI Network", never "VAPI" alone.** First line of every post, every
   watermark. This is the fix for the name collision.
3. **No invented metrics, quotes, case studies, testimonials or client results.**
   If it isn't in a file here or from a cited source, write `[NEEDS DATA: ...]`.
4. **Never publish externally without explicit per-item approval.** Drafting is safe;
   posting, DMing and scheduling are not.
5. **Never freelance on compliance.** Regulation, securities, custody, tax and
   jurisdiction questions get escalated to the client, not answered.
6. Read `01-strategy/voice-and-tone.md` before writing any copy, and check the
   banned-words list before you finish.

## Voice, in one line
A senior engineer explaining something they find genuinely interesting, to a smart
person who doesn't work in crypto. Calm, specific, no hype. No emoji bullets, no
"excited to announce", no token or price talk.

## Where things go
| | |
|---|---|
| `00-pitch/` | Meeting materials for the trial pitch |
| `01-strategy/` | Client profile, ICP, pillars, voice, KPIs, research |
| `02-linkedin/` | Calendar, post bank, templates, engagement playbook |
| `03-podcast/` | Playbook, per-episode folders, templates |
| `04-design/` | Brand guidelines, asset specs, briefs |
| `05-ops/` | Weekly workflow, chat map, reporting |
| `logs/` | Auto-captured prompts and transcripts — do not edit by hand |

## How work gets started
One job per session, via the slash commands in `.claude/commands/`.
See `05-ops/chat-map.md`.
