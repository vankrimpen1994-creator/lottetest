# vAPI Network — project instructions

Read this before any work in this folder. Full research: `01-strategy/client-profile.md`.

## Who the client is (get this right — there's a name collision)
**vAPI Network** (`vapinetwork.ai`) — "onchain task market for agents and humans".
**A platform where you hire agents or humans for scoped work at a fixed price, paid
through USDC escrow.** Both sides sign the scope and price, the buyer locks USDC,
accepted work releases payment, and disputes go to three reviewers (two matching votes
release, refund or split). Products: **Tasks** (the core proposition), **Call** (live —
discover and pay x402 APIs), Compute and Stake (roadmap).

**They are NOT `vapi.ai`**, the voice-AI company (YC W21, $50M Series B, 1M+ devs).
Different company. When researching, always disambiguate.

## Hard rules
1. **Lead with the hiring proposition, never the protocol.** The story is scoped work,
   fixed price, escrow, review, disputes. x402 and the non-custodial plumbing are *proof
   it works*, introduced later in a post — never in the hook. If the first two lines
   contain "x402", rewrite them.
2. **Never claim ship dates for Compute or Stake.** Confirm Tasks' public availability
   before writing copy that assumes anyone can use it today.
3. **Always "vAPI Network", never "VAPI" alone.** First line of every post, every
   watermark. This is the fix for the name collision.
4. **No invented metrics, quotes, case studies, testimonials or client results.**
   If it isn't in a file here or from a cited source, write `[NEEDS DATA: ...]`.
5. **Never publish externally without explicit per-item approval.** Drafting is safe;
   posting, DMing and scheduling are not.
6. **Never freelance on compliance.** Regulation, securities, custody, tax and
   jurisdiction questions get escalated to the client, not answered.
7. Read `01-strategy/voice-and-tone.md` before writing any copy, and check the
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
