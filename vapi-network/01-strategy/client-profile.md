# Client Profile — vAPI Network

_Researched 2026-09-20, corrected 2026-09-21. Sources at the bottom. Anything unverified
is marked `[UNVERIFIED — confirm]`._

## What they are

**vAPI Network** (`vapinetwork.ai`) — homepage line:
> "Onchain task market for agents and humans."

**The core proposition, in the client's own framing:** a platform where you **hire agents
(or humans) for scoped work at a fixed price, paid through USDC escrow.**

This is the headline. The x402 payment plumbing underneath is *how* it works, not *what
it is.* Content that leads with the protocol rather than the hiring proposition is
pitched at the wrong altitude.

### The Tasks flow — the thing to explain over and over
1. Work is scoped. **Both sides sign the scope and the price.**
2. The buyer **locks the agreed USDC in escrow.**
3. Work is delivered and reviewed.
4. **Accepted work releases payment** and records the outcome.
5. **A dispute goes to three reviewers. Two matching votes release, refund, or split the escrow.**

That's a complete, legible story for a business audience — fixed price, money held safely,
a review step, and a defined way to settle a disagreement. It maps onto problems every
company already has with freelancers and contractors. **This is the spine of the content plan.**

### The wider product set
| Product | What it does | Status |
|---|---|---|
| **Tasks** | Post scoped work, fund it in USDC escrow, review before payment, 3-reviewer dispute resolution | Core proposition `[UNVERIFIED — confirm live status: the repo lists Tasks as "next", the site describes the flow in the present tense]` |
| **Call** | Discover x402 APIs, read live price, approve the USDC amount, pay the service directly | Live |
| **Compute** | — | Roadmap |
| **Stake** | — | Coming soon |

**Content rule:** lead with Tasks (the hiring + escrow story). Use Call as proof the rails
already work. Don't claim ship dates for Compute or Stake.

### Supporting facts we can safely use
- Agents can "discover services, pay in stablecoins, hire specialized agents or humans, and receive results **without accounts, dashboards or manual workflows.**"
- **Non-custodial.** Key generated locally, encrypted under a passphrase, never leaves the machine.
- Spend policy applied **before** signing. Caps per wallet, per call, per day.
- Payment routes **directly** to the service. vAPI does not hold funds or proxy payments.
- Receipts to a **local append-only ledger**. No telemetry off the machine by default.
- **Security audit by Hacken.** **Apache 2.0**, open source.
- Chains: EVM (Base mainnet, Arc testnet) and Solana. Settlement in **USDC**.
- Interfaces: `vapi` CLI, **MCP server** (Claude, Claude Desktop, Cursor), TypeScript SDK, gateway (preview).

### Category context (credibility ammunition)
- **x402** launched by Coinbase, May 2025. Governance moved to the **Linux Foundation, April 2026** — 22 launch members including Google, Visa, Mastercard, Stripe, AWS, Circle.
- Coinbase reported **69,000 active agents and 165M transactions** by late April 2026.
- >80% of x402 payments settle on **Base**, almost all in **USDC**.

## The name collision (a real, fixable problem)

`vapi.ai` is a different company — voice-AI infrastructure, YC W21, **$50M Series B in May
2026**, 1M+ developers. On LinkedIn, where search is heavily name-match weighted, typing
"VAPI" surfaces them, not vAPI Network.

Mitigations, all free, all Week 0:
1. Page name is **"vAPI Network"**, never "VAPI" alone; tagline carries "onchain task market"
2. "vAPI Network" in every post's first line and every image watermark
3. Own `#x402` / `#agenticpayments` / `#agenteconomy`, never `#vapi`
4. Claim the custom page URL immediately

## The agency: Coconnect

We work for **Coconnect**, not for vAPI directly. Facts from the intro call (2026-09-26):

- Founded December 2025, boutique — three people on strategy plus freelancers.
- Specialism: growing **real user bases** for Web3 projects. Rik's stated ethos: vanity
  metrics don't count. "It doesn't matter how many clicks you get unless these users are
  actually deploying capital, actually using the product."
- **Compensation is success-based**, tied to product milestones rather than a monthly
  retainer. That is why quality matters to him disproportionately: if the social layer
  underperforms, his own fee is at risk.
- Services: community management, podcasting, SEO, influencer marketing, community
  distribution. Social content is a **new** line they've just started selling in.
- Prior campaigns named: Outcome (prediction markets), dYdX. Onboarding four new clients
  in October; vAPI is the first to take the social scope.
- **Rik** — co-founder, our contact for this trial. **Baha** — CMO, the day-to-day contact
  once onboarded. Weekly client call with all department heads; separate internal
  Coconnect calls that are blunter about what's working.
- For the first campaign, client contact stays with Coconnect. Direct client contact comes
  later, once the fit is proven.
- Work is **freelance and lumpy** by his own description — "one month you have three
  clients, the next nobody." Not a contract.
- Everything runs on **Telegram**.

### The division of labour — this is the brief
Coconnect handles the **freelancer (supply) side** themselves, plus an outreach team,
podcasting and paid ads. Our LinkedIn scope is the **business (demand) side**: getting
companies to bring their hiring to vAPI. A smaller freelancer-facing stream runs alongside
so the two sides of the marketplace can see each other.

Rik's own description of the product, which is the altitude to write at:
> "It's a job board, kind of like Upwork or Fiverr. That's what they are. They're not very
> Web3 native."

## Open questions
- Is Tasks live to the public today, or in private beta?
- Which side is the constraint right now — buyers posting work, or agents/humans to do it?
- Who are the current users, and can we cite any of them?
- Is there a token, raise or launch in the next 90 days to build a calendar around?
- Does a LinkedIn company page exist? Who would post from personal profiles?

## Sources
- https://vapinetwork.ai/ · https://vapinetwork.ai/about _(both egress-blocked from this environment — **verify directly**)_
- https://github.com/vAPI-Network/vapi-network
- https://x.com/vAPI_Network
- https://www.alchemy.com/blog/how-x402-brings-real-time-crypto-payments-to-the-web
- https://www.leadrpro.com/blog/vapi-s-50m-raise-puts-voice-ai-into-b2b-lead-generation

> **Note:** `vapinetwork.ai` is blocked by this environment's network egress proxy, so the
> site could not be read directly. Everything above comes from the GitHub repo, search
> results and ecosystem sources. **Confirm the homepage and /about copy before use.**
