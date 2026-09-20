# Client Profile — vAPI Network

_Researched 2026-09-20. Every claim below is sourced. Anything unsourced is marked
`[UNVERIFIED — ask on the call]`._

## What they actually are

**vAPI Network** (`vapinetwork.ai`) — positioning line on the homepage:
> "Onchain task market for agents and humans."

They are **not** `vapi.ai`, the voice-AI company. See "The name problem" below — this
is the single biggest LinkedIn-specific issue and our opening insight on the call.

### The product, in plain English
An open-source, **non-custodial TypeScript toolkit** that lets a person or an AI agent
discover and pay for APIs using one wallet, over the **x402** payment protocol.
From the GitHub repo:
> "One wallet, every x402 API. Non-custodial agent client, MCP server, CLI and gateway
> for Call, Tasks and Compute."

### The four products and their real status
| Product | What it does | Status |
|---|---|---|
| **Call** | Finds x402 APIs, reads the live price, asks the buyer to approve that USDC amount, pays the service directly | **Live today** |
| **Tasks** | Post scoped work, fund it in USDC escrow, review the result before payment. Disputes go to 3 reviewers; 2 matching votes release, refund or split | Next / coming soon |
| **Compute** | — | Roadmap |
| **Stake** | — | Coming soon |

**This matters for content:** only *Call* ships today. Our content calendar must not
imply Tasks/Compute/Stake are live. Pre-launch products get "building in public"
treatment (roadmap, design decisions, waitlist), not "buy now" treatment.

### Technical facts we can safely say in content
- Non-custodial. Private key generated locally, encrypted under a passphrase, **never leaves the machine**.
- Spend policy applied **before** signing. Caps per wallet, per call, and per day.
- Payments route **directly** from the local wallet to the service — vAPI does not hold funds or proxy payments.
- Receipts written to a **local append-only ledger**. No telemetry off the machine by default.
- **Security audit completed by Hacken.**
- **Apache 2.0**, open source.
- Chains: EVM (Base mainnet, Arc testnet) and Solana. Settlement in **USDC**.
- Interfaces: `vapi` CLI, **MCP server** (works with Claude, Claude Desktop, Cursor),
  TypeScript SDK (`@vapi-network/core`, `@vapi-network/sources`), gateway (`vapi serve`, preview).
- Roadmap: local gateway daemon with per-key budgets, OpenTelemetry tracing,
  task/compute payment tools, discovery expansion (x402scan, Coinbase Bazaar).

### The category tailwind (our credibility ammunition)
x402 is not a fringe standard, and this is the fact that makes the whole thing
legible to a LinkedIn B2B audience:
- Launched by **Coinbase**, May 2025.
- **x402 Foundation** formed with Cloudflare, 2025. Core members include
  **Google, Visa, AWS, Circle, Anthropic, Vercel**.
- Governance moved to the **Linux Foundation, April 2026** — 22 launch members
  including Google, Visa, **Mastercard, Stripe**, AWS, Circle.
- Coinbase reported **69,000 active agents and 165M transactions** by late April 2026.
- >80% of x402 payments settle on **Base**, almost all in **USDC**.

## The name problem (open the meeting with this)

`vapi.ai` is a different, much larger company: voice-AI infrastructure, YC W21,
**$50M Series B led by Peak XV announced May 2026** ($72M total), 1M+ developers,
2.7M agents created, 1B+ calls.

Consequences on LinkedIn specifically:
- LinkedIn search is heavily name-match weighted. Typing "VAPI" surfaces the voice-AI
  company and jobs in Vapi, Gujarat. vAPI Network is invisible.
- Any "VAPI" hashtag or mention is diluted by a company with orders of magnitude more volume.
- Prospects who Google after seeing a post land on the wrong company.

**Mitigations we propose (Week 0, costs nothing, immediate):**
1. Company page name is **"vAPI Network"** — never "VAPI" alone. Tagline carries
   "onchain task market" so the preview card disambiguates.
2. **Every post's first line** and **every image watermark** uses "vAPI Network".
3. Own a distinct hashtag set (`#x402`, `#agenticpayments`, `#agenteconomy`) rather
   than `#vapi`.
4. Secure the LinkedIn page custom URL/handle now, before someone else does.
5. Consistent bio line across every employee profile so the page gains name authority.

`[UNVERIFIED — ask on the call]` Is a rebrand or name change on the table? It changes
how hard we push name-building vs. category-building.

## What we still need from them
- Does a LinkedIn company page exist already, or is it genuinely zero?
- Which founders/execs will post from **personal** profiles? (See `kpi-framework.md` —
  this is the #1 determinant of whether the numbers land.)
- Brand assets: logo files, fonts, colour hexes, any existing deck.
- Who approves content, and how fast? (Target: 48h turnaround.)
- Is there a token, a raise, or a Tasks launch date in the next 90 days? Those are
  content moments we'd build the calendar around.
- Do we get access to the founders for podcast hosting, or are we producing only?

## Sources
- https://vapinetwork.ai/
- https://github.com/vAPI-Network/vapi-network
- https://x.com/vAPI_Network
- https://www.alchemy.com/blog/how-x402-brings-real-time-crypto-payments-to-the-web
- https://www.leadrpro.com/blog/vapi-s-50m-raise-puts-voice-ai-into-b2b-lead-generation
- https://vapi.ai/
