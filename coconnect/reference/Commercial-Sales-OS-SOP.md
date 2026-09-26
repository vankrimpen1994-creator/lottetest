# The Commercial Sales OS. Standard Operating Procedure.

**How to build the five components of an AI-run commercial department, in order, and know when each one is done.**

Version 1.0, 24 September 2026. Built from the Alex van Krimpen (Appic) and Aryan Dua (BenAI) build sessions, 3 August to 21 September 2026, the AI Commercial OS Playbook v1.0 (20 August), and the Appic Germany Sales OS as it stands on disk today.

---

## 0. How to use this document

The system has five components. Each one is a chapter. Each chapter has the same shape:

1. **What it is**: one paragraph, in plain words.
2. **Done means**: the test that says the component is finished.
3. **Build steps**: the SOP, in order.
4. **Hard rules**: the rules that came from real mistakes. Do not soften them.
5. **The Appic reference build**: what exists today, where it lives, and its status.
6. **Open items**: what is still not finished at Appic. Every one of these is a gap you will meet with the next client.
7. **Deliverable**: what you hand over.

Build the components in the order given. Each one feeds the next. Component 5, the second brain, is listed last because it is the container. In practice you create its folder on day one and fill it as you go.

Two delivery modes run through the whole document, same as the Playbook:

- **DWY (Done With You)**: the client does it, you guide. Use it for anything that needs their business knowledge: ICP, schema, copy, stage rules.
- **DFY (Done For You)**: you build, they approve. Use it for anything that needs tooling knowledge.

For the vocabulary (skill, plugin, connector, MCP, CLI, context, tokens, routine), the environment setup and the GitHub gate, read Part A of `AI-Commercial-OS-Playbook.md`. This document does not repeat it.

### The map

```
COMPONENT 1            COMPONENT 2              COMPONENT 3
Lead prospecting  -->  Personalised outreach -->  Automated responses
source, qualify,       cadence, variables,        reply triage, proposal,
enrich, import         sequencer, sending         handover to a human
        |                      |                          |
        v                      v                          v
COMPONENT 4  Reporting and control centre: what went out, what came back, what to do next
        |
        v
COMPONENT 5  The second brain: the folder, the context, the routines, the memory that holds all of it
```

### The weekly rhythm the whole system runs on

| When | What | Component |
|---|---|---|
| Friday 15:00 | Lead prospecting runs. Sheet lands in Slack. | 1 |
| Friday 15:00 to 17:00 | Human review of the sheet. Approve, correct, reject with a reason. | 1 |
| Monday morning | Approved rows imported to the CRM. Leads pushed into the sequencer. | 1, 2 |
| Monday | Campaign starts on the new batch. | 2 |
| Every weekday | Replies triaged, drafts written, human sends. | 3 |
| Every weekday 08:00 to 09:15 | Morning routine, campaign metrics, hygiene, dashboard. | 4 |
| Tuesday and Friday 17:00 | Call scoring. | 4 |
| Friday 16:00 | Optimizer audit of the OS itself. | 5 |
| 1st of the month | Monthly report. | 4 |

Keep the Friday human review. It is not a crutch. It is what lets everything after it be automatic.

---

# COMPONENT 1. Lead prospecting

## What it is

One command produces a list of new, qualified, non-duplicate organisations with reachable decision makers, every week, in a fixed sheet format, and a second command puts the approved rows into the CRM. Nothing writes to the CRM without a human looking at the sheet first.

## Done means

- The sourcing skill runs unattended on a schedule and posts a sheet link to Slack.
- The sheet has the same columns, in the same order, every run.
- 0 of the rows are already in the CRM (checked against organisations, persons and the run registry).
- A human reviews the sheet in under an hour and rejects fewer than 30% of rows.
- The import skill creates CRM records from the approved sheet behind an approval gate, with every field mapped.

## Build steps

### 1.1 Write the ICP as gates and weights (DWY)

The client writes this. You interview it out of them. Three things go in:

**Gates.** A gate removes the lead. Appic's gates, locked on 3 September 2026: paid tickets, a recurring programme, music only (electronic first), an Instagram account, more than 10,000 Instagram followers, and not already in the CRM. No Instagram means reject. There is no follower-count proxy for attendance. Free-entry events (Volksfeste, city festivals) are out even at 500,000 visitors: there are no tickets to resell.

**Weights.** A weight ranks what survives. Attendance sets the tier. Genre carries 20 of 100. For clubs and promoters, event cadence carries 32 points and the tier floor is 50 events a year.

**Timing.** A festival inside 3 weeks of its date is too late to start. Under 90 days the offer changes from the app to promotion only. Clubs have no timing gate.

**The commercial formula, in numbers.** For Appic: a festival says yes, gives tickets at a named release, and that is worth X in GMV. Write it. The AI cannot score value without it.

Tiers: Tier 1 and Tier 2 get contacted. Tier 3 never appears in the sheet. Do not keep it "for later" in the CRM: it pollutes the pipeline.

### 1.2 Pick and weight four to six data sources (DFY)

Do not let the skill search everywhere. Appic's festival sources and weights: festival-alarm 40%, festivals United 25%, festivalticker 20%, ticket.io 10%, festivalhopper 5%. Appic's club and promoter sources: Resident Advisor (public GraphQL), DICE (sitemap and venue pages), Xceed (city pages). All free, plain curl, no key.

Build a separate skill per source family. Appic split festivals from clubs on 1 September because one skill with both crossed the 200k token line and because the scoring differs (attendance versus cadence). They share one run registry so a club skill never resurfaces a festival the other one shipped.

### 1.3 Build the dedupe in three layers (DFY)

1. **CRM organisations**, matched on name stems that align at the start, plus organiser keys and event aliases. Short names collide (CDV versus CD&V) and parents slip through (Goodlive owns several festivals). Two guards, not one.
2. **CRM persons**, by surname. Festival operators run several companies, so a person exists under another organisation more often than you expect.
3. **The run registry** (`runs/registry.json`), so a festival shipped in week 3 does not come back in week 7. Normalise umlauts before you key it: Förderverein and Foerderverein became two entries at Appic.

A match on any layer is a reject with the reason written in the row.

### 1.4 Enrich the organisation, then the people (DFY)

Organisation fields: website, Instagram handle and follower count, attendance or capacity, next event date, ticketing provider, existing app (yes, no, which), region, genre.

Person fields: name, role, direct email, generic company email as the guaranteed fallback, phone, LinkedIn URL, Instagram handle. Find more than one person per organisation. A secondary decision maker doubles the reachable surface and gives the cadence a name to drop.

Tools: Lusha for person data (paid; a personal phone costs 5 credits, so gate it), Firecrawl through its connector for pages, Apify for Instagram followers and LinkedIn URLs (curl cannot read Instagram and Firecrawl refuses the domain). In Germany the Impressum (§5 TMG) guarantees a working email on every commercial site, so "no email" for a German account is a parser failure, not a fact. Impressum emails are obfuscated (`office***(at)***domain`), so the parser must decode them.

Report the fill rate every run. Appic's honest starting point was 11 of 19 organisations fully enriched. Most blanks are structurally absent, not fetch failures: audit the values that are there before you chase the ones that are not.

### 1.5 Fix the sheet as the contract (DWY)

One Google Sheet, two tabs. Appic's: `ORG+DEAL INPUT` (29 columns) and `PERSON INPUT` (8 columns), colour graded, built from a manifest, never by hand. Freeze the header. Give the skill the sheet as its output specification.

Write the person tab RAW, not USER_ENTERED: a phone number that starts with `+` is read as a formula and destroyed.

Columns nobody used in three weeks get deleted.

### 1.6 Build the sourcing skill with a scope cap (DFY)

Walk the whole process once by hand in a chat: source, dedupe, qualify, enrich, publish. Then say "make a skill out of this". Cap the run at 30 to 50 organisations, with a floor of 30 reachable contacts. Unbounded runs at Appic took over 90 minutes and produced worse results.

The skill's five hard rules, from Appic's SKILL.md: a check that cannot confirm returns unknown, never no. Never invent a value. Attendance is the only size gate. Never write to the CRM. Nothing is silently dropped: every rejected candidate carries its reason.

Expect it to grow: 33 reference files, Python scripts, sub-agents. Build a selftest for every parser and know that selftests pass while parsers drift: three of Appic's returned empty or wrong values with no error. Add a live-value assertion per source.

Last step of the skill is a handover, not an import: at Appic, step 8 posts the event websites to the content team's Slack channel, one event per message, only after the link has been fetched and opens.

### 1.7 Build the import skill as a separate skill (DFY build, DWY rules)

Input: the approved sheet. Output: organisations, persons, and either deals or leads in the CRM.

- Map every field explicitly in a table. Create custom fields in the CRM by hand first. Know which object holds each field: at Appic the seven German fields live on the organisation, not the deal, and an org key inside a deal payload is silently ignored.
- Duplicate check before every write, on organisations and on persons.
- Approval gate before any write. No partial imports. Never overwrite a value a person typed. Never invent a select option.
- Mark the channel. Appic sets `channel_id = Claude` so skill imports are separable from hand-typed records.
- Run the local CRM match before every import, even on a sheet the skill itself produced. 12 of 33 rows on one Appic sheet were already in the CRM.
- Never wire the CRM to the sequencer. Activities in the CRM and steps in the sequencer stay separate; a daily sweep reconciles them.

Cold outreach goes into the **Leads inbox**, not the deal pipeline. A lead becomes a deal when it responds. Agreed at Appic with Sven on 21 August. `addLead` takes no custom fields, so the event date goes in the lead title and everything else on the organisation.

### 1.8 Run the tightening loop every week (DWY)

1. Run. 2. Open the sheet. 3. Mark every row high value or reject. 4. Write the exact reason in a column, not "bad fit" but "attendance under 3,000 and no ticketing provider". 5. Paste the reasons back into the skill's chat. 6. Tighten the rules. 7. Ship the new version.

Appic went from 45 loose leads to 20 that survived a tighter filter in two rounds. Fewer, better. Sell this loop; it is the thing a list broker cannot offer.

### 1.9 Schedule it, local first, then cloud (DFY)

Local scheduled task on Friday 15:00 first. Move it to a cloud routine once GitHub access exists and one local run is clean. Cloud has no disk, so the skill and the registry live in a repository and the registry is committed back after every run. Cloud sandboxes block outbound HTTP except pypi, npm and Anthropic; connectors bypass this, curl does not. A scrape that "finds nothing" in the cloud is a network block, not a market fact.

Cloud runs cannot upload a spreadsheet through the Drive connector (the whole xlsx would have to travel as base64 in one argument). Publish the sheet through Composio's Google Sheets connector instead: 1,160 cells in one call, verified.

Keep the Mac task on until the cloud routine produces one good sheet. Never run both.

## Hard rules

1. **Perfect the data before you automate the write.** The CRM upload came out of the sourcing skill on 13 August because bad rows were landing in the CRM. It never went back in.
2. **Gates remove, weights rank.** A missing gate fact is unknown, not a pass and not a fail; flag it and lower the score.
3. **Music only, Instagram required, Tier 3 never ships.**
4. **Three-layer dedupe: organisations, persons, registry.** Name-only matching passes accounts the team already owns.
5. **The sheet is the only render input.** Run fixtures invent contacts.
6. **No CRM field, no scoring weight.** If the CRM cannot hold a value, the skill can still find it, but it lands in a field-gap note, not a score.

## The Appic reference build

| Piece | Where | Status (24 Sep 2026) |
|---|---|---|
| Festival sourcing skill | `Second Brain Appic/Skills/appic-lead-gen/`, installed at `~/.claude/skills/appic-lead-gen/` | Live. Friday 15:00 local task `appic-weekly-festival-leads`. |
| Club and promoter skill | `Skills/appic-lead-gen-platforms/` | Live, run by hand. 708 promoters, 62 and 38 venues enumerated. |
| ICP gate | `icp_gate.py`, runs twice in the skill; rules in `Appic Germany Sales OS/Context/icp.md` | On `main` since 3 Sep. |
| Run registry | `Second Brain Appic/runs/registry.json`, shared by both skills | Live. Umlaut bug open. |
| Master sheet | Google Sheet `1pWw397sOcOpbYxBMGZ3IPr2pZJVjDqadkBp0Jr5-eiQ`, 149 orgs, 336 contacts | The render input for outreach. |
| Import skill | `~/.claude/skills/germany-appic-pipedrive-import/` | Live. Still creates deals in pipeline 11 stage 68; must switch to `addLead`. |
| Account completeness skill | `Skills/pipedrive-account-completeness/` | Live. Runs before any cadence. |
| Cloud routine | `github.com/alexappic/appic-lead-gen-cloud`, trigger `trig_01WzTHYzZjAWz21LxyRUfpZe` | Draft, not enabled. Needs 5 connectors and full network access. |

## Open items

- Import skill still creates deals. The Leads-inbox switch (SOP `pipedrive-pipeline-stages.md`, 21 Aug) is written but not executed.
- Cloud routine has never produced a sheet. Cutover order is in `docs/cutover.md`.
- Apify is connected (5 Sep) but not wired into the skills, so follower counts and tiers are "part guess".
- `registry.py key()` strips umlauts and creates duplicates.
- Sheet `Description` is sales text, so the ICP gate passes non-music events (MYLE, Jazzopen). Check Genre by hand until the gate reads the right column.
- RA's Instagram field is always null.
- The 14 September duplicate miss: a person who had already declined got messaged because the check searched organisations only. Now: persons, Lemlist and Gmail, plus a Peter review, before every send.

## Deliverable

A written ICP with gates, weights and the commercial formula. One sourcing skill per source family. A shared run registry. A master sheet template. An import skill with a field map and an approval gate. A weekly scheduled run. A fill-rate number reported every week.

---

# COMPONENT 2. Personalised outreach campaigns

## What it is

A multichannel sequence, written once by a human, personalised per lead by variables the AI fills from real data, built in a sequencer, and started every Monday on the new batch. The AI never writes the message. It fills the blanks.

## Done means

- A cadence table exists: every touch with its day, channel, purpose and fallback.
- Copy exists for every touch, approved in the review language and rendered in the send language by the same code.
- A renderer produces the sequencer's import columns from the master sheet with no empty `{variable}` and no invented fact.
- Every leaf of the campaign tree has been walked and every claimed touch linted.
- The sequencer campaign is live on a paid plan, with the right sender, and the first batch has run.
- A human is notified of every manual step (Instagram DM, call) and of every reply.

## Build steps

### 2.1 Mine what already works (DWY)

Collect the client's most successful email, Instagram and WhatsApp exchanges and the list of existing customers in the target market for name-dropping. Correct the AI when it misidentifies who is a client: at Appic, 15 signed German app partners exist; Glücksgefühle and Zamna are promotion-only and must never be named as app clients. Some groups are locked to competitors (FKP Scorpio and Glücksgefühle run Appmiral). Resolve group ownership before any German festival is worked.

### 2.2 Design the cadence (DWY)

Appic's shape: 14 touches, 5 channels, 24 to 28 days. Channel order Instagram, LinkedIn, email, WhatsApp, with the cold call moved from day 20 to day 5 on 24 August. It opens with a routing question ("who is the right person for this?") and pitches later. Cold calling is standard in Germany; ask, do not assume, in every market.

Each later touch names the earlier ones: "we emailed you, we DM'd you on Instagram, we connected on LinkedIn". Build the cross-reference into the template, not into the AI's improvisation.

Segment by channel availability, not by persona. Appic runs two campaigns: **A** for leads reachable through public channels (email, Instagram, phone) and **B** for leads with a LinkedIn profile, LinkedIn first. Email is sent regardless of whether the LinkedIn invite is accepted. Six emails is the cap. Day 24 withdraws the invite and hands the lead to a 30-day re-engagement campaign.

Sequence order that matters: biggest events first, swept west to east, no region consolidated. Contact 3 to 6 months before the event.

### 2.3 Templatise the copy, personalise the variables (DWY)

> "AI can personalise variables. AI can't personalise full emails. We don't want AI to do that." Aryan, 18 August.

The human writes one skeleton per channel per step. The renderer fills: `{first_name}`, `{organisation}`, `{next_event_name}`, `{next_event_date}`, `{days_until_event}`, `{current_ticketing_provider}`, `{current_app}`, `{instagram_followers}`, `{secondary_decision_maker}`, `{city}`.

Pick one hook per lead from a ladder and cap any hook at a third of a batch. Hooks with no data behind them are not hooks: Appic dropped City and has never had data for Direktkanal or Artist.

Render copy from the brand name, never from the scraped event name: the scraped name carries its capture year, so one sentence ends up naming two different years.

### 2.4 Build the fallback ladder in the renderer, not the sequencer (DFY)

The sequencer has no logic. It substitutes `{{column}}` and stops. Every fallback, every conditional sentence, every "if no LinkedIn then extra email" is decided in the renderer and arrives in the sheet as a finished sentence.

| Missing | Fallback |
|---|---|
| First name | Organisation name or the team greeting |
| LinkedIn | Campaign A instead of B |
| Phone | Skip the call, move WhatsApp earlier |
| Direct email | Generic company email; every German site has one by law |
| Instagram | Start at email |
| Personalisation hook | The event-date hook; it is always available |

The worst-case message is short and redirect-shaped. Detail kills the reply.

**Greeting follows the address, not the name we hold.** Only a local part that carries the person's name gets `Hey {first name}`. `info@`, `presse@`, `booking@` get `Hey Team`, even when a contact name sits on the record. The primary contact of a row is the person whose address is used; firstName and closer follow that person.

### 2.5 Review in one language, send in another, from the same renderer (DWY review, DFY code)

Appic reviews in English (`--lang en`) and sends in German (`--lang de`). One renderer, two output languages. Never hand-translate an approved sentence. Once Peter approved the German on 1 September, German became the source and English follows it.

The send-language style rules are code, not a note: nine German rules in `references/german-style.md`, enforced by the linter. A review renders one lead but there are 61 strings; lint all of them.

Every draft in the operator's voice passes the voice skill's linter and rubric (Component 5 owns the voice skill). No em dashes. No sign-off. One block.

### 2.6 Test on ten deliberately varied leads (DFY)

Some with everything. Some with only a generic email. Check every fallback fires and no message renders with an empty variable. Appic tested the ladder on 62 leads on 20 August and 10 Tier 2 leads on 1 September. First result: 10 sent, 1 reply.

### 2.7 Build the campaign in the sequencer (DFY)

Lemlist is the sequencer. Facts learned at Appic that will repeat:

- **Instagram is not a Lemlist channel.** It is a manual task. Drive it with a browser automation, 10 to 30 a day, or a human.
- **A manual step still blocks sender assignment.** Delete the typed step; do not toggle it manual. An empty `list_mailboxes` is not proof of no mailboxes.
- **The API appends conditions but refuses edit, delete and insert-at-index.** Build trees top to bottom, never reorder. `update` on a field-check delay returns success and keeps the old value; delete and re-add.
- **Gates go on the parent condition, not inside the branch,** or gated-out leads lose the wait.
- **`create` echoes "running"; the campaign is a draft.** Confirm with the next step call.
- **A withdrawn LinkedIn invite cannot be resent inside a 24-day cadence.** Move that touch off LinkedIn.
- **Never wire the CRM to Lemlist.** Lemlist cannot create CRM activities. A daily sweep reconciles.
- **Task wrapper text is copy too.** Step instructions are hand-written and outside every check. Write them in the send language and lint them.
- **Live in Lemlist is not approved.** A Facebook step reached a reviewer that way. The tree also changes between two reads on the same day; read it again before you ship.
- **Walk every leaf before launch.** On Appic's LinkedIn branch, Email 1 never sent because one leaf was never wired. Found 20 September.

### 2.8 Sender and deliverability (DFY)

At 30 to 50 contacts a week from a company mailbox the risk is low. Above that, buy a secondary domain and warm it. Set the sender explicitly per campaign and check it: Appic's Reeperbahn campaigns went out from `alex@` instead of `business@` on 16 September and, once paused, kept sending through 18 September according to Gmail. Paused is not stopped until the sequencer's own log says so.

### 2.9 Notify the human of manual tasks and replies (DFY)

The system must interrupt only when it matters: an Instagram DM or call is due, a prospect replied, a deal has gone quiet. Route to Slack. The mechanism Aryan and Alex agreed on 3 September: webhook triggers through Make.com (or n8n) into cloud routines, not time-based polling. Lemlist had zero webhooks configured on 12 September; that setup is the first task of Component 3.

## Hard rules

1. **The AI fills variables. The AI never writes the message.**
2. **The robot never sends to a prospect.** `outbound.robot_may_send_to_prospect: false`, decided 4 September. The OS reads Lemlist; it never starts, stops or sends a campaign.
3. **Copy is reviewed in English and sent in German from the same renderer.** No hand translation.
4. **Every fallback lives in the renderer.** The sequencer has no logic.
5. **Greeting follows the address, not the name.**
6. **Never say downloads come through Appic's own reach.** Installs come through the organiser's channels. Appic's side of the trade is that the organiser keeps learning about their visitors all year. A Belgian client saw the other framing as feeding visitors to later festivals.
7. **The pitch is relevant 365 days a year,** not the festival week: engagement in the app plus every event in one place.
8. **Short-notice events (under 90 days) get the promotion offer, not the app.**
9. **Never ask the festival to change its event.** Appic carries the logistics or drops the idea.
10. **Every draft passes the voice linter and rubric.** Below 80 means redraft.

## The Appic reference build

| Piece | Where | Status (24 Sep 2026) |
|---|---|---|
| Cadence SOP (14 touches, 5 channels, 28 days) | `Second Brain Appic/Departments/International Sales and Business Development/sops/germany-cold-outreach-cadence.md` (18 Aug) | Active but behind the skill (v4/v5, Campaigns A and B). |
| Cadence skill and renderer | `Skills/german-outbound-cadence/` (`build_personalisation.py`, `render_touches.py`, `enrich_from_impressum.py`, `from_master_sheet.py`) | Live. `references/lemlist-columns.md` stale: 22 documented, 41 actual. |
| German copy and style rules | `Resources/templates/german-outbound/`, `references/german-style.md` | Approved by Peter 1 Sep. German is the source. |
| Campaign v5 TEST | Lemlist | Running. 10 sent, 1 reply. Manual steps show zero. |
| Campaign A (public channels) | `cam_5y6BPdYZDYnDX3RhS` | Draft, built 3 Sep. 57 of 149 organisations qualify. |
| Campaign B (LinkedIn first) | `cam_TdGNNuT5o7Fo78kgN`, plan in `Skills/german-outbound-cadence/runs/2026-09-17-campaign-B-plan.md` | Draft, rebuilt 17 Sep with Miona's branching. 14 gates, 24 days. Three items must be done by hand in the UI. |
| Re-engagement campaign | `Wiedervorlage 30 Tage` | Empty. |
| Campaign records | `Appic Germany Sales OS/Campaigns/*.md`, matched on `lemlist_id` | Counters stopped 5 Sep; one synced 17 Sep. |
| Second sending domain | `business@beappic.com` | Planned 1 Sep; sender mix-up 16 Sep. |
| Voice skill | `~/.claude/skills/alexs-voice/` | Live. `email-de` register unmeasured. |

## Open items

- Campaigns A and B are drafts. No production batch has run.
- `ticketing_line` still splices English prose into German sentences.
- German director titles are not ranked; the grammatical-gender question is open.
- Hook guard counts hook text instead of `hook_src`.
- Lemlist connector disconnected 19 and 23 September; typed calls failing 24 September. `cam_bB2ZeD4TeqFBb2mco` sits empty and unbuilt.
- Manual-task alerts (Instagram, calls) to Slack: agreed 3 September, not built.
- Instagram browser automation: not built.
- The activity sweep between Lemlist and Pipedrive: not built.
- Amplifire replied and booked a meeting on 10 September; Lemlist still shows 0 meetings. Replies are not being marked.

## Deliverable

A cadence table. Copy per channel per step in review and send language. A renderer with the fallback ladder and the style linter. A variable list. Two campaigns live in the sequencer with the right sender. A test log of ten varied leads. A Slack alert for every manual task and every reply.

---

# COMPONENT 3. Automated responses

## What it is

When a lead replies, the system reads the reply, decides what kind it is, drafts the answer in the operator's voice and in the lead's language, and puts it in front of a human to send. When a discovery call happens, the system reads the transcript and drafts the proposal email. Nothing is sent by a robot. The hour after a reply, and the hour after a call, happen by themselves up to the send button.

## Done means

- Every positive, neutral and negative reply lands in Slack within the hour with a draft attached.
- Every discovery call that agreed on a proposal produces a Gmail draft and a Slack DM within two hours.
- The human edits fewer than one in three drafts before sending.
- Edits flow back into the voice skill.

## Build steps

### 3.1 Decide the handover point (DWY)

At Appic: handover to a human happens at the first reply. From then on the sequencer stops for that lead and a person owns the thread. Write this down; it sets everything below.

### 3.2 Write the reply playbooks (DWY)

For each reply type, the client writes what a good answer does. Appic's positive-reply rules, learned from real replies:

- **"We already have an app."** Stay curious. Never sell against what they have. Ask who they built it with and where it fell short. Use the answer as the reason for a call.
- **"Send more info."** One or two lines, never a deck.
- **"Meet us at event X."** If Appic is not attending, decline plainly and counter with two or three concrete slots read from the live calendar. Never invent attendance.
- **"Our event is too close."** Kills the app pitch, not the promotion offer. Under 90 days is a different offer.
- Lead with the 365-day relevance and the year-round learning about visitors, never with Appic's own reach.

Negative and neutral replies get a template each: thank, close the loop, park with a re-engagement date.

### 3.3 Build the reply triage routine (DFY)

Trigger: a reply webhook from the sequencer (or, until webhooks exist, an hourly weekday poll). The routine:

1. Reads the reply and the thread.
2. Classifies: positive, neutral, negative, out of office, wrong person.
3. Picks the playbook.
4. Drafts the answer in the lead's language, in the operator's voice, through the voice skill.
5. DMs the operator on Slack with the classification, the draft and the deal link.
6. Never sends. Never touches the sequencer or the CRM.

Set up the webhook first. The relay is Make.com or n8n calling the cloud routine trigger with a bearer token and the Anthropic API version header. Appic's Lemlist had zero webhooks on 12 September, so the routine exists as a prompt and nothing fires it.

### 3.4 Build the proposal email routine (DFY)

Trigger: a new transcript in the notetaker, through the same relay, with an hourly weekday cron as backup.

Gate: **no draft unless the call itself agreed that a proposal is the next step.** Only the operator can force past it. The routine reads the transcript, the Gmail thread and the CRM record, answers the objections raised on the call inside the mail, chooses one of the two shapes that have shipped (Appic: the Bootshaus shape for clubs, venues and promoters; the Blacklist shape for a single festival), attaches the rate card as a Drive link, and leaves a Gmail draft plus a Slack DM.

Rules that came from real drafts: the tier must not change inside the mail (the 4 September Blacklist mail did). Never say "Dutch database" (Sophie). Lightweight proposals without formal contracts close faster in a new market; do not force the home-market document. The email is the proposal.

Three places change together: the template, the config and the routine prompt.

### 3.5 Daily inbox triage (DFY)

A weekday routine reads overnight email, summarises what arrived, drafts replies in the operator's voice, and leaves everything as drafts. When the human edits a draft before sending, that edit is training data. Feed it into the voice skill's draft log.

### 3.6 Notifications, not dashboards (DFY)

Interrupt the operator only for: a prospect replied, an important email arrived, a proposal draft is ready, a deal went quiet past the stale threshold, the weekly lead sheet is ready. Everything else waits for Component 4.

## Hard rules

1. **A robot never sends to a prospect.** Draft plus DM, always.
2. **No proposal draft without the call agreeing on a proposal.** Operator-only override.
3. **Handover to a human at the first reply.**
4. **Stay curious; never sell against what they already have.**
5. **Never claim Appic's reach drives the downloads.**
6. **Decline events Appic is not attending; counter with live calendar slots.**

## The Appic reference build

| Piece | Where | Status (24 Sep 2026) |
|---|---|---|
| Proposal draft skill | `Second Brain Appic/Skills/appic-proposal-draft/` | Live, readable master. |
| Proposal email routine | `Appic Germany Sales OS/Routines/proposal-email.md`, templates in `Templates/proposals/` (Bootshaus, Blacklist) | PENDING. Cloud routine deleted 12 Sep for rebuild; trigger not wired (`proposal-email-trigger-setup.md`). Was live every 2 hours from 3 Sep. |
| Lemlist reply triage routine | `Routines/lemlist-reply-triage.md` plus setup file (12 Sep) | PENDING, not created. Zero Lemlist webhooks. |
| Post-disco follow-up (generic) | `~/.claude/plugins/sales-os/skills/post-disco-followup/` | Replaced. Installed, no routine calls it. |
| Reply playbooks | Root `CLAUDE.md` rules 19 to 22 in `Second Brain Appic` | Written as assistant rules, not yet as routine inputs. |
| Daily inbox triage | Planned in Playbook 9.2 | Not built as a routine. |

## Open items

- Webhook relay (Make.com or n8n to cloud routine trigger): agreed 3 September, not configured for Fireflies or Lemlist.
- Reply triage routine: prompt exists, never created.
- Proposal routine: deleted for rebuild, not recreated.
- Reply playbooks live as rules in `CLAUDE.md`; they need to become a reference file the triage routine reads.
- Daily inbox triage: not built.
- The voice skill's `email-de` register is unmeasured, and every reply in Germany is `email-de`.

## Deliverable

Written reply playbooks per reply type. A reply triage routine wired to a webhook. A proposal email routine wired to the notetaker. A daily inbox triage. Slack notifications for replies and drafts. A draft log that feeds the voice skill.

---

# COMPONENT 4. Reporting and the control centre

## What it is

One page and one Slack feed that say what went out, what came back, where every deal stands, what it is worth, and what to do next. The numbers arrive without anyone asking. The page reflects the client's real business model, not a generic SaaS dashboard.

## Done means

- A morning routine runs every weekday before the operator opens the laptop and posts to Slack.
- The dashboard shows the last completed week first, then today, and is reachable on a public URL.
- Outbound metrics (sent, opened, replied, meetings, per channel, per campaign) and pipeline metrics (deals per stage, moved, new, closed, stale, value) sit on the same page.
- The forecast is labelled as a prediction and named after the thing the business actually earns.
- A deal that has gone quiet is flagged, never auto-closed.
- Every number on the page has a source the operator can open.

## Build steps

### 4.1 Write the business model into the config first (DWY)

For Appic: revenue is tickets resold, so the commercial metric is GMV and the forecast is "Predicted GMV forecast", never "revenue". Rate card: four German tiers from €829 to €3,495 paid in tickets. Owner IDs resolve to names, never raw numbers. Pipeline IDs: 11 Germany, 8 New Business NL, 14 Belgium, 2 Account Management NL. Stage IDs change; read won from status, never from a stage ID list (three stage IDs in `config.md` stopped existing on 4 September).

If the source of record for the commercial metric is not connected (Appic: Perdoo holds the Q3 key results and nothing reaches it), the page says so and dates the last real number. It never invents.

### 4.2 Define the pipeline stages with hard rules (DWY)

Eight stages in every country. For each stage, the one thing that is genuinely true when a deal sits there. "Proposal sent" means the document went out. "Closed" at Appic is post-event. Stale: 30 days silent is flagged; 3 to 6 months is archived, never deleted. To park a deal: mark Lost, label Prospect, schedule an activity two months out.

Do not turn on any automatic deal movement until the rules are signed. Bart owns the written CRM policy at Appic; changes are amendments to his doc.

### 4.3 Build the morning routine (DFY)

Weekdays 08:00. Reads the CRM, the calendar, yesterday's transcripts and the sequencer. Writes one deal file per active deal, prepares a call brief for every call today (disqualify first: free admission is checked before size), captures yesterday's calls, reconciles tasks. Posts a short brief to Slack. Scope: the operator's own deals only.

### 4.4 Build the campaign metrics sync (DFY)

Weekdays 08:20. Reads every campaign in the sequencer and writes per-campaign counters (sent, opened, clicked, replied, meetings, per step, per channel) into the OS. This is the "what went out" half of the control centre. It depends on the sequencer connector being attached to the routine, and on replies being marked in the sequencer (Component 3).

### 4.5 Build pipeline hygiene (DFY build, DWY rules)

Weekdays 08:45, after the morning routine. Writes the pipeline snapshot, the week file and the trends file. Flags deals silent 30 days. Posts to the sales report channel. No real CRM writes until the stage rules are signed and the routine has run in read-only mode for at least two weeks.

### 4.6 Build the dashboard (DFY)

Weekdays 09:15, last in the chain because it reads everything the others wrote. Five tabs at Appic: Today, Pipeline, Context, Capabilities, Stack. The Pipeline tab leads with the last completed week (Sven, 8 September). Fills a fixed template of slots, deploys to a public page (appic-de-pipeline.vercel.app), posts the link.

Brand it only after the numbers are right. Aryan stopped Alex from styling a report before the content was checked. Zero is drawn as the word "none", never as an empty cell.

Ask what decision the page should trigger. Appic's requirement of 20 August still stands: accurate data is there; revenue forecasting and decision alerts are what is missing. A page that only says what happened is a report; a page that says what to do next is a control centre.

### 4.7 Call scoring and win-loss (DFY)

Tuesday and Friday 17:00: score every first call the operator ran on seven weighted dimensions (Appic: 25, 15, 15, 15, 10, 10, 10, summing to 100; diagnosis before pitch carries 25). Every grade is backed by a verbatim quote. Do not trust the notetaker's speaker labels; match by content. Never invent a score.

Monthly: win-loss. Reclassify no-reply losses near the event date as timing losses. Exclude value-0 deals from averages (98% of pipeline 11 carries no value). Stages 73 and 74 hold deals the team already calls closed, so won undercounts.

### 4.8 Monthly and quarterly reports (DFY)

1st of the month 09:00: monthly report plus a losses file. Quarterly on 1 January, April, July, October. Name files `YYYY-MM-monthly.md`. The monthly management deck and the meet-up deck are separate skills built from the previous deck, never from a template.

### 4.9 Audit every routine before handover (DFY)

Open a fresh chat, attach the OS folder, and ask it to explain every routine: sequence, logic, what, when, why. Correct everything that does not match reality. Budget half a day. Appic's 4 September audit found three dead stage IDs, a missing methodology file, and that all seven routines ran locally with no CRM writes, which the docs did not say.

## Hard rules

1. **Reports are on the operator's own deals only** (`owner_id 27929623` at Appic).
2. **Robots make no real CRM writes until the stage rules are signed.** Flag, never auto-close.
3. **The forecast is labelled a prediction and named after the real metric.** GMV, not revenue.
4. **Review the numbers before you brand the page.**
5. **Owner IDs and stage IDs are resolved from the live API, never from a list in a doc.**
6. **A routine's enabled state lives on the trigger.** Query it; never trust a repo line.
7. **Run order is a dependency.** Morning, metrics, hygiene, dashboard. A late morning run ships a brief with no call prep.

## The Appic reference build

| Routine | Schedule | Where | Status (24 Sep 2026) |
|---|---|---|---|
| Morning | Mon to Fri 08:00 | `Appic Germany Sales OS/Routines/`, ids in `Context/config.md` under `execution.cloud_twins` | Cloud since 5 Sep. Local disk stopped updating 5 Sep; output goes to the Baalda server. |
| Campaign metrics | Mon to Fri 08:20 | same | Lemlist connector not attached. |
| Context refresh | Mon 08:30 | rewrites `Context/live/targets.md` | Cloud. |
| Pipeline hygiene | Mon to Fri 08:45 | posts to `#germany-sales-report` (C0BUSHZU823) | Cloud. Stale rule changed 22 Sep to flag only. |
| Dashboard | Mon to Fri 09:15 | `Dashboard/template.md`, 28 slots; appic-de-pipeline.vercel.app | Cloud. Gap analysis in `Dashboard/GAP-ANALYSIS-2026-09-04.md`. |
| Call scoring | Tue and Fri 17:00 | `Calls/`, `Deals/`; weights in `Context/config.md` | Cloud. Stage list in the skill is outdated. |
| Monthly | 1st 09:00 | `Reports/` | Only `sales-report-2026-08.md` exists; wrong name pattern; says it could not open local files. |
| Quarterly | 1 Jan/Apr/Jul/Oct | `Reports/` | Never run. |
| Optimizer | Fri 16:00 | audit and score DM | Cloud. `Reports/audits/` empty. |
| DE pipeline report skill | on demand | `anthropic-skills:appic-de-pipeline-report` | Live. |

## Open items

- Outbound metrics are not on the page. The Lemlist connector is not attached to the metrics routine, and replies are not marked in Lemlist.
- Revenue (GMV) forecasting and decision alerts: requested 20 August, still missing.
- The commercial source of record (Perdoo) is not connected; the 28K GMV figure is a 7 July Q2 number.
- `Context/live/week.md` and `trends.md` are listed in `MAP.md` but do not exist on disk.
- `Reports/analysis-methodology.md` is missing.
- Six of seven deal files sit on a colleague's Pipedrive record, so the scope rule excludes them.
- Local disk and Baalda vault disagree; empty local folders are not proof a routine failed. Read the log in the vault.

## Deliverable

A config file with the business model, owner map, pipeline map and stage rules. Nine scheduled routines in dependency order. A hosted dashboard with the last completed week first. A Slack feed. A monthly report. One completed routine audit.

---

# COMPONENT 5. The second brain

## What it is

The folder that holds everything: the static context a human writes once, the live context the routines rewrite every day, the skills, the routines, the outputs, the memory, and the house rules. It is what makes every run better than the last, because the context accumulates in one place and every skill reads it.

## Done means

- One folder, one `CLAUDE.md` at the root and one in every subfolder that has its own rules.
- `Context/` is human-owned and no routine writes there. `Context/live/` is robot-owned and overwritten.
- Every routine is a cloud routine that reads and writes the folder through a vault connector, with the local copy disabled.
- A `MAP.md` describes the structure and is updated on any structural change. A `MEMORY.md` is a dated, append-only log.
- The operator can open a fresh chat, attach the folder, and ask it to explain the whole OS, and the answer matches reality.

## Build steps

### 5.1 Create the folder on day one, separate from the company vault (DFY)

Start the Sales OS as its own folder, not inside the general knowledge base. Keeping it separate during the build stops one broken thing from breaking everything. Merge later once stable. Appic runs two: `Second Brain Appic` (the company vault: people, departments, skills, tasks, daily notes) and `Appic Germany Sales OS` (the OS: deals, calls, campaigns, routines, dashboard).

Decide the rule for when they disagree. At Appic: the company vault wins on company facts. Tasks never live in the OS; they go to the vault task list. Skills stay in the vault; the OS calls them.

### 5.2 Lay out static and dynamic context (DWY)

```
Sales OS/
├── CLAUDE.md          house rules and routing
├── MAP.md             structure; updated on any change
├── MEMORY.md          dated append-only log
├── Context/           STATIC. 8 docs, human-owned. icp, offer, sales-process,
│                      stack, config, brand, team, strategy. "No routine ever writes there."
│   └── live/          DYNAMIC. targets, pipeline snapshot, losses. Robot-owned, overwritten.
├── Deals/             one file per deal, {Organisation}.md, plus _pipeline-snapshot.md, metrics.md
├── Calls/             one file per call, YYYY-MM-DD-{org}.md
├── Campaigns/         one file per sequencer campaign, matched on lemlist_id
├── Routines/          one prompt file per routine, plus manifest.md
├── Reports/           logs, audits, archive; YYYY-MM-monthly.md
├── Templates/         proposals/, outreach/ (indexes the vault master, holds dated snapshots)
├── Dashboard/         template.md with fixed slots, index.html
└── config/            offer.md, pandadoc.md
```

Every folder gets a `CLAUDE.md` with its own conventions. Frontmatter on every file: type, date, status, org or deal id, owner, tags. Deal files carry `pipedrive_deal_id`, `package_tier`, `face_value`, tickets, `event_date`. Call files carry `fireflies_id`, `call_type`, `ran_by`, `excluded_reason`, scored.

### 5.3 Write the house rules as rules, not prose (DWY)

The root `CLAUDE.md` holds the routing table (every kind of information has one home; no catch-all) and the numbered rules. Every operator correction becomes a permanent numbered rule the same day. Appic's root has 23 rules, from "never use em dashes" to "greeting follows the address". Rules that the code can enforce move into the code (linters, gates) and stay in the doc as the reason.

### 5.4 Build the voice skill first among the skills (DWY)

Everything the OS writes passes through it. Build it from a real corpus: sent email, WhatsApp, Instagram and Slack messages, dictated speech, LinkedIn posts. Appic's was calibrated on 103,626 words. It has two gates: a deterministic linter (banned phrases and structures, no em dash, no sign-off, one block) and a 100-point rubric judge; below 80 means redraft. It classifies the register first (typed message, cold email, warm email, proposal, Spanish, German). Measure every register you use; Appic's `email-de` is still a placeholder.

The build is token-heavy (400,000 tokens in one chat). Run it in its own chat and `/compact`.

### 5.5 Organise skills by function, and keep operator settings out of the skill (DFY)

Buckets that recur: lead generation, outreach, replies, reporting, conferences, content. A folder per one-off project throws context away.

The skill's `SKILL.md` lives where it is installed (`~/.claude/skills/` or a plugin). The vault holds `Skills/{slug}/notes.md`, `run-config.json`, `references/` and dated `skill-source-YYYY-MM-DD/` snapshots. Never edit the plugin cache copy; the cache lags. When the installed copy and the vault snapshot differ (Appic's lead-gen does), the installed one is what runs.

Install `find-skills`, `eli5` and `grilling`: the first finds a skill before you build one, the other two are how you stress-test the OS structure with the operator (Aryan, 3 September).

### 5.6 Connect the stack, and know each connector's limits (DFY)

| Tool | Use | Limit learned at Appic |
|---|---|---|
| Pipedrive | CRM | Notes need raw HTML. Website and Instagram fields are dirty. Custom fields live on the org. Owner and stage IDs resolve from the API. |
| Google Workspace | Sheets, Docs, Gmail, Drive | Use the CLI (`gws-appic`), not the MCP. Cloud runs cannot upload a spreadsheet through Drive. Docx updates in place keep comments. |
| Composio | Sheets from the cloud | Publishes with no key through the connector. Phone columns RAW. |
| Slack | notifications, reports | One request per message for the content team. |
| Fireflies | transcripts | Speaker labels and language unreliable; uploaded recordings have no title. Match by date and content. |
| Lemlist | sequencer | See Component 2. Connector drops; check before every run. |
| Lusha | person enrichment | No German festival coverage; the Impressum beats it 173 to 37. Phone costs 5 credits. |
| Firecrawl | scraping | Two silent failures: 200 from the wrong page, and speaker pages that invert ICP density. Refuses Instagram. |
| Apify | Instagram followers, LinkedIn URLs | Connected, not wired. |
| Baalda Vault MCP | the OS folder in the cloud | Org-level connector, `c121e737`, Sales OS only. Cloud can lead local disk. Never add a local duplicate. |
| GitHub | cloud routines with code | Enterprise org access is an admin request with lead time. A cloud routine needs its own GitHub connection; local `gh` auth does not count. |
| Vercel | hosting the dashboard | |
| Make.com or n8n | webhook relay into cloud routines | Agreed 3 Sep, not configured. |

Set every connector to Always allow, or you click 100 prompts per run. On macOS, Documents access is a privacy grant; asking for a folder mid-session can kill access to all of `~/Documents` for the session.

### 5.7 Move routines to the cloud, one at a time, never both (DFY)

Local scheduled task first. When one run is clean and the connectors exist in the cloud, create the cloud twin as a draft, review it, enable it, and disable the local copy. Record the routine IDs in `Context/config.md` under `execution.cloud_twins`. The enabled state lives on the trigger: query it, never trust a doc line. A routine update replaces the whole job config; resend the whole block or the trigger returns 400.

Two ways to reach a folder from the cloud: a vault connector (Baalda, for the OS files) or a GitHub repository (for skills with code, like lead gen). Appic uses both.

Cloud runs read and write through the connector; the local disk may lag or stop. Since 5 September the Appic OS on disk has not updated while the routines run. Read the log in the vault, not the folder.

### 5.8 Keep the memory and the map (DFY)

`MEMORY.md` in the OS: dated, append-only, one line per fact. The assistant's own memory directory outside the vault holds what the repo does not: connector limits, corrections, decisions with dates. Every correction from the operator is saved the same day. Consolidate monthly.

`MAP.md`: what each folder holds, what each routine writes, in what order. Update it on any structural change. Appic's still says Lemlist is out of scope and lists two live files that do not exist. A stale map is worse than none: the optimizer routine audits against it.

### 5.9 Roll out to the team (DWY)

Pilot with the commercial department. `Context/` is company property; voice skills are per person. Every skill has a named owner who reviews its output monthly. Teach the tightening loop, not the buttons. Weekly: check outputs. Monthly: retire dead skills, tighten live ones. Then copy the architecture to the next department.

## Hard rules

1. **No routine ever writes to `Context/`.** Humans own static context.
2. **Never run the local and cloud copy of a routine at the same time.**
3. **The company vault wins on company facts.** Tasks live in the vault, never in the OS.
4. **Every operator correction becomes a numbered rule the same day.**
5. **Run the vault skill, not the plugin cache.**
6. **Keep any chat and any skill under 200,000 tokens.** Split above it.
7. **Never run a skill naked.** Read it, give it context, then run.

## The Appic reference build

| Piece | Where | Status (24 Sep 2026) |
|---|---|---|
| Company vault | `~/Documents/Second Brain Appic/` | Live. Root `CLAUDE.md` with 23 rules and the routing table. |
| Sales OS vault | `~/Documents/Appic Germany Sales OS/` | Live in the cloud through Baalda since 5 Sep 14:22. Local disk stale since 5 Sep. |
| Static context | `Appic Germany Sales OS/Context/` (8 docs) | Human-owned. |
| Live context | `Context/live/` | targets and losses exist; week and trends do not. |
| Routine manifest | `Routines/manifest.md`, `Context/config.md` | 9 cloud routines, ids under `execution.cloud_twins`. |
| Voice skill | `~/.claude/skills/alexs-voice/`, notes and addendum v009 in the vault | Live. |
| Assistant memory | `~/.claude/projects/-Users-Business-Documents-Second-Brain-Appic/memory/` | 100+ facts, indexed in `MEMORY.md`. |
| Cloud lead-gen repo | `~/Documents/appic-lead-gen-cloud`, `github.com/alexappic/appic-lead-gen-cloud` | Private, pushed. Routine draft. |
| Skills | `Second Brain Appic/Skills/` (17 folders), plus `~/.claude/skills/` and the `sales-os` plugin | Live. Lead-gen installed copy differs from vault snapshot. |

## Open items

- `MAP.md` is stale (Lemlist out of scope; two phantom live files).
- Local and cloud OS copies disagree since 5 September. No sync check exists.
- Two skills (win-loss, call scoring) still list 10 pipeline stages; 7 exist.
- `Calls/2026-09-01-Ankerberg-Festival.md` is 0 bytes and duplicates another file.
- The Sales OS plugin's setup interview has been run once. A second operator (Peter, Sophie) has not been onboarded.
- Webhook relay for event-driven routines: not configured.

## Deliverable

Two folders with `CLAUDE.md` in every subfolder. A `MAP.md` and a `MEMORY.md`. A voice skill with linter and judge. Every connector live and set to Always allow. Every routine in the cloud with its local twin disabled. One completed audit in which the OS explained itself correctly.

---

# PART D. Running the build

## D1. Build order and time

| Order | Component | Days | Mode | Gate to the next |
|---|---|---|---|---|
| 0 | Second brain: folder, `CLAUDE.md`, connectors, GitHub request | 1 to 2 | DFY | Every connector proven with one real call |
| 1 | Lead prospecting | 5 to 8 | DFY build, DWY tune | One clean sheet that survives human review |
| 2 | Personalised outreach | 5 to 8 | DWY copy, DFY renderer and sequencer | Ten varied leads rendered with no empty variable; every leaf walked |
| 3 | Automated responses | 2 to 3 | DFY | One reply and one call produced a draft in Slack |
| 4 | Reporting and control centre | 3 to 4 | DFY, DWY rules | Morning chain runs four days in a row and the dashboard shows the last completed week |
| 5 | Second brain: cloud twins, memory, map, audit, team | 2 to 3 | DFY, DWY rollout | The OS explained itself correctly in a fresh chat |

Five to six weeks with a daily 30 to 45 minute session. Appic and BenAI met every working day from 3 August. The daily rhythm is the product; weekly calls let a blocker sit for six days. Record every session. This document exists because 30 of them were recorded.

Appic's actual timeline: components 1 and 5 by 20 August, component 2 built in Lemlist by 1 September, component 4 in the cloud by 5 September, component 3 written 12 to 13 September and not yet wired. The order held. The estimate did not: Alex told Oskar on 20 August that the required time was underestimated. Quote six weeks, not four.

## D2. Metrics per component

| Component | Metric | Appic today |
|---|---|---|
| 1 | Qualified organisations per week; % surviving review; fill rate; duplicate rate; run duration | 30 to 50 per run; fill rate 11 of 19 at start; 12 of 33 duplicates on one sheet before the local match |
| 2 | Touches sent per week; reply rate per channel; % of leaves that fire | 10 sent, 1 reply on the first test |
| 3 | Time from reply to draft; % of drafts sent unedited | Not measured; nothing fires yet |
| 4 | Meetings booked per 100 sourced; deals moved correctly versus corrected; forecast versus actual GMV | Not measured; outbound metrics not on the page |
| 5 | Baseline `/context` under 40k tokens; routines audited and matching reality; corrections turned into rules | 23 rules; audit 4 Sep found 3 dead ids |

Lead with hours per 50 leads for the diagnostic and meetings per 100 sourced for the retainer.

## D3. Client prerequisites, send before day one

- GitHub organisation access granted to the AI app (admin request, lead time).
- CRM admin rights to create custom fields.
- A Google account that can create a Cloud project and accept the GCP terms.
- Brand assets. A writing corpus (sent mail, messages) for the voice skill.
- Budget approved: Lusha credits, Apify, Firecrawl, Lemlist Multichannel plan, Vercel, Composio, Make.com or n8n.
- A CRM export for the dedupe rule.
- A second sending domain, or the decision not to have one.
- A named decision maker in every daily session. Not a delegate.

## D4. The daily session

| Minutes | Segment |
|---|---|
| 0 to 5 | Homework tracker. Tick what is done. |
| 5 to 15 | Client shows what they built or ran. |
| 15 to 30 | Work the blocker live. |
| 30 to 40 | Teach one concept. |
| 40 to 45 | Set tomorrow's homework. |

## D5. What this document does not cover

Pricing, offers and the sales narrative for selling the build: Part C of `AI-Commercial-OS-Playbook.md`. Conference and event prospecting: the parallel module in the Playbook, plus the `conference-qualification` skill (score from the programme and speaker pages, never the homepage; under ten conferences a year means a slash command, not a system). The Appic monthly decks: `appic-mt-slides` and `appic-monthly-meetup-slides`.

---

# APPENDIX. Source log

- `AI-Commercial-OS-Playbook.md` v1.0, 20 August 2026, same folder.
- Alex and Aryan sessions after the Playbook: 21 August (10-lead test, 5 usable, Pipedrive reset, second domain), 24 August (Composio for Sheets, master sheet, manual review of leads), 25 August (Lemlist personalisation review, campaign logic, email regardless of LinkedIn accept), 3 September morning (ICP locked to electronic music, 2,000+ attendance, 10,000+ followers, two campaigns by channel availability, Slack alerts for manual tasks), 3 September afternoon (Sales OS review, dashboard layout, webhook triggers through Make.com or n8n instead of schedules, second brain centralises email, calls, CRM, Slack and WhatsApp). 21 September recording captured no content.
- Alex and Oskar (BenAI), 20 August: the OS scope for the cohort, pricing from €5,000, time underestimated.
- `Appic Germany Sales OS/` on disk, 24 September 2026: `CLAUDE.md`, `MAP.md`, `MEMORY.md`, `Context/`, `Routines/`, `Campaigns/`, `Dashboard/`, `Reports/`, `Templates/`, `config/`.
- `Second Brain Appic/Skills/` (12 skills read), `Departments/International Sales and Business Development/sops/` (cadence 18 Aug, pipeline stages 21 Aug), `Team/appic/Profiles/Alex van Krimpen/Daily/` 20 August to 17 September, root `CLAUDE.md` rules 17 to 23.
- `appic-lead-gen-cloud` README.
- The assistant's memory index for the Appic vault, 100+ dated facts from the build.
