# Coconnect commercial OS: build plan

_Version 1, 2026-09-26. This plan follows `reference/Commercial-Sales-OS-SOP.md` (the SOP) and
`reference/AI-Commercial-OS-Playbook.md` (the Playbook), adapted to what we learned on the
[kickoff call](../00-discovery/2026-09-24-rik-kickoff-notes.md). Section numbers such as "SOP 1.3" point into the SOP._

---

## 1. What we are building, in one paragraph

Today Coconnect's deal flow depends on warm intros from a market maker, advisors and partners, plus Bull
Shark on commission. Their own cold outreach is manual and had produced one win in nine months. We
are building the SOP's five components for them:
- A weekly sheet of qualified Web3 projects with reachable decision makers.
- Multichannel sequences personalised from real signals, such as a recent raise, an upcoming TGE or announced volume.
- Replies and proposals drafted automatically, with a human pressing send.
- A dashboard plus a Slack feed.
- A second brain that holds all of it.

We build it twice over, once for each motion: **core packages** and **Hub**.

## 2. How Coconnect differs from the Appic reference build

The SOP was written from Appic (German festivals). These are the places where copying it straight
would break for Coconnect:

| Area | Appic (SOP) | Coconnect | What it changes |
|---|---|---|---|
| Market | Festivals, venues, promoters | Web3 projects: recently funded, heading to TGE, with prediction markets and iGaming the most receptive so far | New ICP gates, new sources, new hook ladder |
| Offers | One (app, or promotion for short-notice events) | **Two motions:** core packages (large campaigns) and Hub ($1k + 10% of prize pool, quick yes, repeat purchases) | Two ICPs, two cadences, two copy sets, possibly two source lists. One shared registry. |
| Channel order | Instagram → LinkedIn → email → WhatsApp → call | Core: **X → LinkedIn → Telegram** (Rik's ranking; email's place still unknown). Hub: **X + Telegram** only | X and Telegram are probably not native lemlist channels (to verify). They become manual or browser-automated tasks, like Instagram at Appic (SOP 2.7). |
| Senders | One mailbox, then a second domain | About 5 verified X accounts (Rik, co-founder, company, CMO, …) | Assign accounts to leads, set daily caps and a warm-up. Volume limits get set during the build. |
| Contact data | The German Impressum guarantees an email; Lusha is weak | Web3 teams are often pseudonymous. X and Telegram handles matter more than emails. | Enrichment ladder: X bio → website/team page → LinkedIn → Telegram → Lusha. Fill rate will be lower. Report it honestly. |
| Timing gate | Event date | Raise date, TGE date, campaign or launch windows | "Days since raise" and "days to TGE" become the timing weights |
| Dedupe | CRM organisations, persons, run registry | The same, **plus Bull Shark's lists and warm and partner intros** | Avoids double-contacting and commission conflicts with Bull Shark and the market maker |
| Commercial metric | GMV | Core package fee, Hub fee plus 10% of prize pool, and Alex's 20% | The forecast is named after the real metric |
| Proof and hooks | 15 named app partners | The Outcome case (to verify), plus Overtime | The case study must be confirmed in writing before it goes into copy |

## 3. The build, step by step

**Owners:** **A** = Alex (DFY, builds it) · **C** = Coconnect (DWY, supplies business knowledge and approves).
Each step ends with a **done test**. Don't start the next step until it passes.

### Step 0. Kick-off and prerequisites (week 0, before the context sprint)
| # | Task | Owner | Input needed |
|---|---|---|---|
| 0.1 | Send the intake questionnaire and the prerequisites list | A | [`../00-discovery/intake-questionnaire.md`](../00-discovery/intake-questionnaire.md) |
| 0.2 | Rik sends his promised doc: ICP, hooks that worked, channel ranking, Hub info | C | — |
| 0.3 | Claude subscription for the Coconnect operator, running Code rather than Cowork (Playbook A3) | C | Who is the operator? |
| 0.4 | Tool budget approved: Firecrawl, lemlist (multichannel plan), enrichment (Lusha or an alternative), Slack | C | — |
| 0.5 | GitHub access for cloud routines. Request it on day zero because it has a lead time (Playbook A4) | C | — |
| 0.6 | Book a daily 30 to 45 minute session slot, with a named decision maker, recorded on Fireflies | A + C | Calendar |

**Done:** the questionnaire is back, the budget is approved, the operator is named and the sessions are booked.

### Step 1. Second brain skeleton (days 1 to 2) — SOP component 5.1 to 5.3, Playbook phase 1
| # | Task | Owner |
|---|---|---|
| 1.1 | Create the Coconnect Sales OS folder or repo: `CLAUDE.md`, `MAP.md`, `MEMORY.md`, `Context/`, `Context/live/`, `Deals/`, `Calls/`, `Campaigns/`, `Routines/`, `Reports/`, `Templates/`, `Dashboard/` | A |
| 1.2 | Connect the stack and set every connector to Always allow: Slack, Google Workspace, Fireflies, CRM, Firecrawl, lemlist | A |
| 1.3 | Prove each connector with one real call (post a Slack test message, read a CRM record, pull a Fireflies transcript) | A |
| 1.4 | Check that `/context` at rest stays under 40k tokens | A |

**Done:** every connector has answered one real call.

### Step 2. Context sprint (week 1, daily 30 minutes) — SOP 1.1, 2.1, 4.1, 5.2; this is the "week of drilling" Alex promised
This week produces the static `Context/` documents. Coconnect writes them, and Alex interviews the content out of them.

| Day | Session focus | Output file |
|---|---|---|
| 1 | Business model and offers: core packages vs Hub, what a yes is worth, the revenue formula | `Context/offer.md`, `Context/business-model.md` |
| 2 | ICP, core motion: gates, weights, timing, walk-away signals | `Context/icp-core.md` |
| 3 | ICP, Hub motion: gates, weights, the fast-yes profile | `Context/icp-hub.md` |
| 4 | What worked: the best DMs and emails, the hooks, the Overtime story, name-droppable clients, channel results | `Context/proof-and-hooks.md`, `Templates/outreach/examples/` |
| 5 | Sales process: pipeline stages with hard rules, handover point, proposal timing, team roles and X accounts | `Context/sales-process.md`, `Context/team.md` |

Also this week: collect the **writing corpus** for the voice skill (sent DMs, emails, Telegram messages, X posts)
from whoever sends the messages (SOP 5.4).

**Done:** all the Context files are written, and Rik has read and signed off each one.

### Step 3. Lead prospecting (weeks 2 to 3) — SOP component 1
| # | Task | Owner | Coconnect specifics |
|---|---|---|---|
| 3.1 | Turn the ICP into gates and weights and a tier definition (SOP 1.1) | C writes, A structures | Candidate gates: raised within N months, TGE ahead or recent, sector in scope, active X account, not already in the CRM or Bull Shark or warm pipelines. Candidate weights: raise size, sector fit (prediction markets and iGaming first), X followers and engagement, days to TGE. |
| 3.2 | Pick and weight 4 to 6 sources (SOP 1.2) | A proposes, C approves | Candidates to test: "ICO Analytics" (named by Alex on the call), CryptoRank and RootData funding rounds, DefiLlama raises, ICO Drops, and the X timeline for announced volume. Each gets verified for access, cost and cloud reachability. |
| 3.3 | Three-layer dedupe plus Bull Shark and warm-intro lists (SOP 1.3) | A | Key the registry on the normalised project name **and** the X handle, because projects rebrand and change ticker |
| 3.4 | Enrich the organisation, then 2 or more people (SOP 1.4) | A | Org: website, X handle, followers, raise (amount, date, lead investors), TGE date, chain, sector, Telegram group. People: CEO or founder, Head of Marketing or Growth, BD, each with their X, Telegram, LinkedIn and email. |
| 3.5 | Master sheet as the contract: an `ORG` tab and a `PERSON` tab, built from a manifest, with the person tab written RAW (SOP 1.5) | C owns columns, A builds | Add a `motion` column (core or hub) and an `x_sender` column |
| 3.6 | Walk the full process by hand once, then turn it into a skill. Cap each run at 30 to 50 orgs (SOP 1.6) | A | One skill per source family if it goes past 200k tokens |
| 3.7 | Import skill with a field map and an approval gate. Cold leads go to the Leads inbox, not the deal pipeline (SOP 1.7) | A builds, C sets rules | Depends on the CRM decision (build-time) |
| 3.8 | Tightening loop every week: every row gets approve or reject, with the exact reason (SOP 1.8) | **C** | Rik's team does the Friday review |
| 3.9 | Schedule it: local Friday 15:00 first, cloud later (SOP 1.9) | A | Sheet link goes to Coconnect's Slack |

**Done:** one clean sheet survives human review with fewer than 30% of rows rejected and no duplicates.

### Step 4. Personalised outreach (weeks 3 to 5) — SOP component 2
| # | Task | Owner | Coconnect specifics |
|---|---|---|---|
| 4.1 | Mine what already works (SOP 2.1) | C | Rik's best X DMs and LinkedIn messages, the Overtime thread, client names they may drop |
| 4.2 | Cadence tables, **one per motion** (SOP 2.2) | C designs, A structures | Core: X-first, LinkedIn next, Telegram last, and email's place to be decided. Hub: X plus Telegram, shorter, and it asks for the yes sooner. Split campaigns by channel availability, the same pattern as Appic's A and B. |
| 4.3 | Templates written by Coconnect, variables filled by the AI (SOP 2.3) | C writes | Variables: `{first_name}`, `{project}`, `{raise_amount}`, `{raise_date}`, `{lead_investor}`, `{tge_date}`, `{days_to_tge}`, `{sector}`, `{x_followers}`, `{announced_volume}`, `{secondary_contact}`. Hook ladder: sector case (prediction markets and iGaming), recent raise, upcoming TGE, announced volume, generic. Cap any one hook at a third of the batch. |
| 4.4 | Fallback ladder lives in the renderer (SOP 2.4) | A | For example: no X handle means start on LinkedIn, and no LinkedIn means use Telegram or email |
| 4.5 | Voice skill with a linter and a rubric, built from Coconnect's corpus (SOP 2.5, 5.4) | A builds, C supplies corpus | Probably one voice per sending account |
| 4.6 | Test on 10 leads with deliberately varied data (SOP 2.6) | A + C | — |
| 4.7 | Build in lemlist and walk every leaf (SOP 2.7) | A | X and Telegram steps become manual tasks or browser automation. Set per-account daily caps during the build. |
| 4.8 | Sender setup: X accounts per lead, and a secondary email domain if email is used (SOP 2.8) | A + C | — |
| 4.9 | Slack alert for every manual step (X DM, Telegram) and every reply (SOP 2.9) | A | Uses a Make.com or n8n webhook relay |

**Done:** 10 varied leads render with no empty variable, every leaf has been walked, and the first batch is live.
Alex's promise of "a first test run in 2 to 3 weeks" is the first real batch.

### Step 5. Automated responses (week 5) — SOP component 3
| # | Task | Owner |
|---|---|---|
| 5.1 | Decide the handover point. Default: at the first reply, a human owns the thread | C |
| 5.2 | Reply playbooks per reply type, e.g. "we already have a marketing agency", "send deck", "what did Outcome get?", "only interested in Hub", plus not now, wrong person, out of office | C |
| 5.3 | Reply triage routine, fired by a webhook. It drafts and DMs the operator and never sends | A |
| 5.4 | Proposal routine: a Fireflies transcript leads to a Gmail draft and a Slack DM, **only when the call agreed on a proposal**. One shape each for core and Hub | A builds, C supplies proposal templates |

**Done:** one real reply and one real call have each produced a draft in Slack.

### Step 6. Reporting and control centre (weeks 5 to 6) — SOP component 4
| # | Task | Owner |
|---|---|---|
| 6.1 | Write the business model into the config: fees, Hub formula, 20% commission, owners, pipelines | C |
| 6.2 | Pipeline stages with hard rules, signed off (see Step 2 day 5) | C |
| 6.3 | Morning routine, campaign metrics sync, pipeline hygiene and dashboard, run in that order on weekdays | A |
| 6.4 | Dashboard showing leads sourced, touches sent per channel and account, replies, meetings booked per 100 sourced, pipeline value per motion, and the last completed week first | A |
| 6.5 | Call scoring and monthly report | A |

**Done:** the morning chain runs four days in a row and the dashboard shows the last completed week.

### Step 7. Cloud, audit and handover (weeks 6 to 8) — SOP 5.7 to 5.9
| # | Task | Owner |
|---|---|---|
| 7.1 | Move each routine to the cloud one at a time, then disable its local twin | A |
| 7.2 | Audit: in a fresh chat, have it explain every routine, and correct whatever doesn't match reality | A + C |
| 7.3 | Train Coconnect's team on the tightening loop, not on the buttons | A |
| 7.4 | Start the ongoing rhythm: Friday review, Monday launch, monthly skill review | C |

**Done:** the OS explains itself correctly in a fresh chat, and the first meetings from the engine are booked.

## 4. Timeline

| Week | Focus | Checkpoint |
|---|---|---|
| 0 | Prerequisites, questionnaire back | Operator named, tools paid |
| 1 | Second brain skeleton + context sprint | Context files signed off |
| 2–3 | Lead prospecting | First clean sheet |
| 3–5 | Outreach build + first test batch | **First test run** (Alex's "2 to 3 weeks") |
| 5 | Replies and proposals | Drafts arriving in Slack |
| 5–6 | Dashboard and reporting | Morning chain green 4 days running |
| 6–8 | Cloud, audit, tightening | **Fully tuned** (Alex's "~2 months") |

**What can slip:** Alex's next two weeks are busy, and there's a large conference in October. The SOP also warns
that its own estimates ran long, so quote six weeks rather than four. If the context sprint slips, everything
after it slips too.

## 5. Decisions we make during the build (parked for now, on purpose)
- **CRM:** which one, and who administers it. Affects step 3.7 and everything in step 6.
- **X sending limits:** per-account daily caps, warm-up, and which account sends to which lead. Affects steps 4.7 and 4.8.
- **Outcome proof:** confirm the figures and the review in writing before they go into any template. Affects steps 4.1 and 4.3.

## 6. Homework tracker (keep it updated at the top of every session)
| # | Task | Owner | Due | Done |
|---|---|---|---|---|
| 1 | Send intake questionnaire + prerequisites to Rik | Alex | | [ ] |
| 2 | Rik's ICP, hooks, channels and Hub doc | Rik | | [ ] |
| 3 | Name the operator and the daily decision maker | Rik | | [ ] |
| 4 | Approve tool budget | Rik | | [ ] |
| 5 | Request GitHub access | Rik | | [ ] |
| 6 | Book daily session slot for context week | Alex + Rik | | [ ] |
