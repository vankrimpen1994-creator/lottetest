# The AI Commercial OS Playbook

**How to build, run and sell an AI-powered business development system.**

Version 1.0 — built from the daily build sessions between Alex van Krimpen (Appic) and Aryan Dua (BenAI), 3 August to 20 August 2026.

---

## 0. How to read this manual

This manual has three layers. Use the layer you need.

| Layer | What it is | Who uses it |
|---|---|---|
| **Part A — Foundations** | The words, the tools, the rules. | Everyone. Read once. |
| **Part B — The Build** | 12 phases, in build order. Each phase is an SOP. | The builder. |
| **Part C — The Business** | How to package, price and sell this. | You, selling it. |

Two delivery modes run through the whole manual:

- **DWY (Done With You)** — you teach. The client clicks. You watch and correct.
- **DFY (Done For You)** — you build. The client reviews and approves.

Each phase says which mode fits best and why.

**One rule above all others:** build in the order given. Each phase feeds the next. If you jump to outreach before the data is clean, you will send bad messages fast. That is worse than sending nothing.

---

# PART A — FOUNDATIONS

## A1. The vocabulary

Learn these seven words. Everything else is detail.

### Skill
A skill is one repeatable job written down as a text file (a markdown file). You give the AI an SOP. The AI follows it every time.

Alex's own definition, from the 7 August session, is the one to use with clients:

> "A skill is a repeatable action that you ask Claude to do, based on an SOP that you have."

A skill is not only for automation. A skill can be four things:

1. **An automation** — do this workflow (lead generation, CRM import).
2. **A context layer** — know this (brand colours, ICP, tone of voice).
3. **A questionnaire** — ask the user these questions and build from the answers (onboarding).
4. **A product** — a game, a report generator, a tool you hand to someone.

A skill is a zip file. Inside is one `SKILL.md` file plus reference files. Reference files can be Python scripts, HTML templates, CSV data, anything. The Appic lead generation skill grew to **33 reference files** and used sub-agents to save context. Aryan called it "a monster of a skill."

### Plugin
A plugin is a bundle of skills plus context. Instead of sending a client 16 separate skills, you send one plugin. This is the unit you sell.

### Connector / MCP / API
- **API** = Application Programming Interface. The set of actions a software tool allows a program to take. Gmail has one endpoint for sending mail, one for reading, one for drafting.
- **MCP** = Model Context Protocol. An Anthropic invention. It bundles all of a tool's API endpoints into one package the AI can use.
- **Connector** = what the MCP looks like inside the AI app. The pathway between the AI and your software.

Order of preference when you want the AI to touch a new tool:
1. Use the **native connector** if it exists.
2. If not, find the **MCP server URL** online and add it as a **custom connector**.
3. If no MCP exists, use the **MCP creator skill**. Point it at the tool's API documentation. It builds the MCP for you.

### CLI
A CLI is a shortcut way to reach a tool without loading a full MCP. MCPs sit in the context window and eat tokens all the time. A CLI only loads when it is needed. CLIs are faster, cheaper and lighter.

Appic uses a Google Workspace CLI (`gws`) for Sheets, Docs and Gmail for exactly this reason.

### Context
Context is everything the AI knows before it starts your task. Two kinds:

- **Static context** — always true. ICP, business model, pricing, brand, strategy, pipeline stage definitions.
- **Dynamic context** — changes daily. New emails, new meetings, new leads, deal movements.

Static context you write once. Dynamic context needs a scheduled job to keep it fresh. This split is the whole design of the Second Brain.

### Tokens and the 200k rule
The AI has a context window. It fills up. As it fills, quality drops.

**The rule: keep any single chat or any single skill under 200,000 tokens of work.** Above 200k–300k the model gets measurably worse, even though the window technically holds a million.

Two commands to manage this:
- `/context` — shows what is using your tokens right now, before you even start. A loaded Second Brain can cost 36,000 tokens at rest.
- `/compact` — spawns a sub-agent, reads the whole chat, summarises it. A 400,000-token chat drops to about 35,000–40,000 tokens. You keep working in the same chat.

**This is your test for splitting a skill.** Walk the process manually with the AI. If it crosses 200k tokens, break it into two or more skills.

### Routine (scheduled task)
A job that runs on a timer.

- **Local routine** — runs on your machine. Your laptop must be awake at the run time. Good for testing.
- **Cloud routine** — runs on Anthropic's servers. Needs a **GitHub repository** instead of a local folder, because the cloud has no access to your disk.

You cannot convert a local routine into a cloud routine. That feature was removed. You must create the cloud routine fresh. Plan for this.

---

## A2. The five rules of building

These came out of three weeks of real mistakes. Give them to every client on day one.

**Rule 1 — Never run a skill naked.**
> "No skill is generally applicable to anyone. You need to personalise each and every skill for yourself." — Aryan, 7 August

Read the skill first. Skim the markdown. Then give it context before you run it. Always.

**Rule 2 — Walk the process manually first, then make the skill.**
Do the whole job by hand in a chat with the AI. When it works, say "make a skill out of this." Use the built-in **skill-creator** skill. Never write a skill from imagination.

**Rule 3 — Split at 200k tokens.**
See above.

**Rule 4 — Do not build a skill for something you do once a year.**
Alex built a conference qualification workflow, then realised Appic attends maybe six conferences a year. Aryan's response:

> "Sometimes you're putting in the effort and you realise it's not worth it, because it's not a recurring thing."

Still make it a slash command if the workflow is already done. Do not invest more.

**Rule 5 — Perfect the data before you automate the write.**
The single biggest lesson of the whole build. Do not let a sourcing skill write into your CRM until the output sheet is clean and approved by a human. Appic had to strip the Pipedrive upload back out of the lead generation skill on 13 August because bad data was landing in the CRM.

---

## A3. The environment

Set this up before Phase 1. It takes half a day.

### Choose your surface
Two ways to run the AI. Know the difference.

| | Cowork | Code (desktop / CLI) |
|---|---|---|
| Speed | Slower | Faster |
| Bugs | More (question loops, resets) | Fewer |
| Installing skills by command | No — give it the file | Yes |
| Internet + autonomy | Limited | Full |
| Recommended for | Light review, non-technical users | Everything else |

Aryan's verdict on 7 August: *"I'm just not a fan of Cowork. It's too slow and it's just these kinds of bugs."*

**Default to Code.** Use Cowork only when a client refuses a terminal.

### Set connector permissions to "Always allow"
Do this first or you will spend your day clicking approvals. Alex clicked close to 100 permission prompts in one lead generation run before this was fixed.

1. Open the connector (Google Drive, Pipedrive, etc.).
2. Find the permissions dropdown that says "Custom — needs approval."
3. Change it to **Always allow**.
4. Repeat for every connector you use.

Leave approval on only where the risk is real.

### One folder to rule them all
Create a single project folder. Appic called it the Second Brain. Everything AI-related lives inside it: skills, context, outputs, notes.

Then attach that folder to your chats and your routines. In any chat there are two separate selectors — do not confuse them:
- One picks **local or cloud** execution.
- One picks **which folder** the chat can see.

### Install skills globally
Install skills at global level, not per project. Then any chat, in any folder, can reach them.

### Install `find-skills`
Go to **skills.sh**. It is a marketplace of over 1.5 million skills, ranked by stars and downloads. The first listing is `find-skills`. Copy the install command and give it to Code.

After that, mid-task, you can say *"find me a skill that will help me do X"* and it will search the marketplace and install the best match.

### Connect the stack
For a sales build, connect these:

| Tool | Purpose | How |
|---|---|---|
| CRM (Pipedrive) | Deals, orgs, people | Native or custom MCP connector |
| Google Workspace | Sheets, Docs, Gmail, Drive | **CLI**, not MCP — see below |
| Slack | Notifications, reports | Native connector |
| Fireflies (or notetaker) | Call transcripts | Native connector |
| Lusha | Contact enrichment | Connector, paid credits |
| Firecrawl | Web scraping | Connector |
| Apify | Structured scraping | Connector |
| Lemlist | Multichannel sequencing | Connector, paid plan |
| GitHub | Cloud routines | Native connector — see A4 |

### The Google Workspace CLI trap
Google Workspace is the hardest install in the whole build. Alex lost most of two sessions to it (5 and 13 August).

You need to:
1. Create a Google Cloud Platform project.
2. Enable the Workspace APIs you need.
3. Accept the GCP Terms of Service.
4. Configure the OAuth consent screen.
5. Create a Desktop OAuth client.
6. Download the JSON credentials.
7. Run the login and verify with a real Gmail call.

**Two known failure modes:**
- **Multiple Google accounts in one browser.** The OAuth flow attaches to the wrong account. Sign out of all but the target account first.
- **Multiple CLI setups colliding.** If you have more than one Workspace CLI on the machine, they overlap and authentication breaks. Write one line into your project's `CLAUDE.md`: *always use the [client] Google Workspace CLI.* That line resolves it.

There is a guided installer skill for this: `google-workspace-cli-installer-guide`. Use it. Do not do this by hand with a client on the call.

---

## A4. GitHub — the gate to the cloud

Every routine starts local. Every routine should end in the cloud. GitHub is the bridge.

**Why:** a cloud routine has no access to your laptop. It needs a repository holding the skill and the connector configuration.

**The blocker to expect:** if your client is on a GitHub Enterprise / organisation account, an admin must grant the AI app access before any repository can be attached. Alex hit this on 20 August and it stopped all cloud work for several days. **Raise this on day one of any engagement.** Put it in the kick-off email as a client prerequisite.

**Setting up a cloud routine (the prompt that works):**

> Check out my weekly lead gen local routine. I want to convert it into a cloud-based routine.
> Create a new GitHub repository to work inside.
> The skill it needs access to is the [Skill Name] — find the most updated version and add it to the repository.
> Work out every connector the skill needs as a prerequisite and add those too.
> Do not turn it on yet. Keep it as a draft and tell me when it is done.

Then you review the draft, and only then activate it.

**Fallback while you wait for GitHub access:** keep running the routine locally. Set the run time for a moment when the laptop is definitely awake.

---

# PART B — THE BUILD

## Build map

| Phase | Name | Days | Mode |
|---|---|---|---|
| 0 | Discovery and bottleneck map | 1 | DWY or DFY |
| 1 | Environment and connectors | 1–2 | **DFY** |
| 2 | Lead sourcing engine | 3–5 | DFY build, DWY tune |
| 3 | Enrichment layer | 2–3 | DFY |
| 4 | Data standardisation | 1–2 | **DWY** — client owns the schema |
| 5 | CRM import and hygiene | 2 | DFY build, DWY rules |
| 6 | Reporting and visibility | 1–2 | DFY |
| 7 | Voice and content | 1 | **DWY** — needs their real writing |
| 8 | Outreach cadence | 3–4 | **DWY** — client owns the copy |
| 9 | Post-call and CRM automation | 2 | DFY |
| 10 | Scheduling: local to cloud | 1–2 | DFY |
| 11 | Sales OS assembly | 2 | DFY, guided interview |
| 12 | Team rollout | 2 | DWY |

Total: about four to five weeks with a daily 30–45 minute check-in. That cadence matters. Alex and Aryan met **every working day**. Momentum is the product.

---

## PHASE 0 — Discovery and bottleneck map

**Goal:** find the one bottleneck that, if fixed, unlocks the most revenue. Build that first.

### Steps

**0.1 — Run the bottleneck interview.** Ask these, in this order:

1. Walk me through your sales process, first touch to money in the bank.
2. Where does it break? Where do deals sit and rot?
3. Which step takes the most human hours per week?
4. Which step is least structured — where does every rep do it differently?
5. What do you already have written down? ICP, qualification rules, templates, brand guide.
6. What tools are you in every day? Which ones hold the truth?
7. How many people will use this? Who owns the CRM?

**0.2 — Name the bottleneck.** For Appic on 3 August it was clear within twenty minutes: **lead generation and qualification were completely unstructured.** No repeatable sourcing. No measurable qualification. Every list built by hand.

**0.3 — Map the full pipeline anyway.** Even though you fix one thing first, draw the whole chain, because it becomes the product roadmap:

`Source → Qualify → Enrich → Import to CRM → Outreach → Meeting → Proposal → Close → Report`

**0.4 — Pick the quick win.** Lead generation is almost always the right first build. It is visible, measurable, and it produces an artefact the client can hold in week one.

**0.5 — Set the meeting rhythm.** Daily, 30–45 minutes. Same time. Same link. Recorded with a notetaker, because the transcripts become the SOP later. (This manual is proof of that.)

**0.6 — Create a homework tracker.** A shared tab with tasks and a done column. Mark which tasks must run in Code and which in Cowork. Review it at the top of every call.

### Deliverable
A one-page bottleneck memo plus a homework tracker with the first five tasks.

### Selling note
Phase 0 is your paid discovery. Charge for it. It de-risks the quote and it is where the client decides they trust you.

---

## PHASE 1 — Environment and connectors

**Goal:** the client's AI can reach every system that holds their truth.

**Mode: DFY.** Do not make a commercial leader configure a Google Cloud OAuth consent screen. You will lose them.

### Steps

1. **Create the master project folder.** One folder. Name it for the business.
2. **Write the first `CLAUDE.md`.** Include: which CLI to use, folder conventions, house rules.
3. **Set every connector to Always allow.**
4. **Install skills globally.**
5. **Install `find-skills` from skills.sh.**
6. **Install the Google Workspace CLI** using the installer skill. Verify with a real Gmail call and a real Sheets write.
7. **Connect the CRM.** Confirm read and write against a test record.
8. **Connect Slack.** Post a test message to the channel that will receive reports.
9. **Connect the notetaker.**
10. **Request GitHub access.** If the client is on an org account, the admin request goes in today. It has a lead time.
11. **Run `/context` on a fresh chat.** Note the baseline token cost. Anything over ~40k at rest means you have too many MCPs loaded — move some to CLIs.

### Checklist to hand the client
- [ ] Master folder created and attached
- [ ] All connectors Always allow
- [ ] Workspace CLI authenticated, one Google account only
- [ ] CRM read/write proven
- [ ] Slack posting proven
- [ ] GitHub org access requested (date: ____)
- [ ] Baseline `/context` under 40k tokens

### Common failures
| Failure | Fix |
|---|---|
| 50–100 permission popups mid-run | Always allow, per connector |
| Workspace CLI auth fails | Sign out of extra Google accounts; one CLI per machine; declare it in `CLAUDE.md` |
| Cloud routine cannot see files | GitHub not connected yet — stay local |
| Chat is slow and forgetful from the start | Too many MCPs; convert to CLIs |

---

## PHASE 2 — Lead sourcing engine

**Goal:** one command produces 30–50 new, qualified, non-duplicate prospect organisations per week.

### 2.1 — Define the ICP in writing
Before any code. The skill is only as good as this document. Capture:

- Geography (Appic: Germany, all regions)
- Entity type (real festivals, paid entry, next edition confirmed, not cancelled)
- Size floor and ceiling (attendance range — agree an explicit valid range)
- Online presence (Instagram followers as a proxy for reach)
- Technology signals (does it already have an event app? which ticketing provider?)
- Exclusions (already in CRM, already a client, dormant)
- **The commercial model in plain numbers.** For Appic: a festival says yes — how many tickets do they give, at which release, what is that worth in GMV? Write the formula. The AI cannot score value without it.

**DWY moment.** The client must write this. You can interview it out of them, but the words must be theirs.

### 2.2 — Choose and weight the data sources
Do not let the skill search "everywhere." Aryan was explicit:

> "I wouldn't do that, because we probably want to limit the scope of the data sources. Otherwise it'll just become much more chaotic."

Pick four to six sources. Give each a **weight** that balances quality against volume. For Appic these were German event and festival databases. Build a separate, broader skill later if you want wide discovery — do not widen this one.

### 2.3 — Build the scoring model
A numeric score, not a vibe. Appic's live weights on 17 August:

| Gate / signal | Weight |
|---|---|
| In target country | Gate |
| Is a real festival, paid entry | Gate |
| Has a confirmed next edition, not cancelled | Gate |
| Not already in the CRM | Gate |
| Attendance size | 35 |
| Online presence (Instagram followers) | Weighted |
| Ticketing provider identified | Weighted |
| Existing app status | Weighted |

Gates remove. Weights rank. Output a tier: Tier 1 / Tier 2 / Tier 3, with an explicit definition of each.

### 2.4 — Build the deduplication rule
The skill must check the CRM before it outputs. Appic's rule became a scoring gate: *"not already Appic"* means not already in Pipedrive.

Also build a **DNC (Do Not Contact) list** — a maintained list of organisations the skill must never surface again. Losing this rule means you contact the same festival three times with three different reps.

### 2.5 — Build the skill
Walk the full process manually with the AI. Source, filter, score, tier, output. Then say: *"create a skill from this process."*

Expect it to be big. Appic's ended at 33 reference files, running Python scripts, using sub-agents to keep context down.

**Set an explicit scope cap in the skill.** How many organisations per run: 30–50 is the working number. Unbounded runs took over 90 minutes and produced worse results.

### 2.6 — The tightening loop (run this weekly)
This is the highest-value habit in the whole system.

1. Run the skill. Get a batch (start with 100–200 to shake out bugs; settle at 30–50).
2. Open the output sheet.
3. Go through every row. Mark **high value** or **reject**.
4. **Write the exact reason in a column.** Not "bad fit" — *"attendance under 3,000 and no ticketing provider found."*
5. Paste that reasoning back into the skill's chat.
6. Ask the AI to tighten the qualification rules based on it.
7. Update the skill.

After two rounds of this, Appic's output moved from 45 loose leads to 20 leads that all survived a tighter filter. Fewer, better. That is the correct direction.

**Sell this loop.** It is the thing clients cannot buy in a tool. It is the reason your system beats their list broker.

### Expected performance
- Run time: 45 minutes to 1.5 hours for a full batch.
- Yield: 20–50 qualified organisations per weekly run.
- Track run duration every time. Rising run time means the skill is bloating.

### Deliverable
A named lead generation skill, a written ICP document, a scoring model, a DNC list, and one clean output sheet.

---

## PHASE 3 — Enrichment layer

**Goal:** turn an organisation into a reachable human, with a reason to talk to them.

### 3.1 — Organisation-level enrichment
Fill these fields for every organisation:

- Website
- Instagram handle **and follower count**
- Attendance / capacity
- Next event date
- Ticketing provider
- Existing app: yes / no / which one
- Region
- Genre or category

Follower count and attendance are the two fields that drive scoring. Insist on them.

### 3.2 — Person-level enrichment
For each organisation, find the decision makers. **Find more than one.**

> Appic's contact rate problem was solved by scraping multiple personas per organisation, not by scraping more organisations.

Per person:
- Full name
- Role / title
- Direct email
- Generic company email (the guaranteed fallback)
- Phone number
- LinkedIn URL
- Instagram handle

Include a **secondary decision maker**. It gives the outreach cadence a name to drop, and it doubles your reachable surface.

### 3.3 — Wire the enrichment tools
| Tool | Use | Note |
|---|---|---|
| **Lusha** | Person contact data | Paid credits. **Monitor the burn rate.** Assign an owner. |
| **Firecrawl** | Website and page scraping | Good for structured public pages |
| **Apify** | Structured scraping at scale | Improved Appic's data quality noticeably when added |
| **Public web fallback** | When enrichment tools are absent | The skill falls back to publicly available data on its own — it works, it is just thinner |

Authenticate them fully. A half-connected Lusha silently returns nothing and you will blame the skill.

### 3.4 — Handle the gaps honestly
You will never get 100% fill. Appic's real number on 14 August: **11 of 19 organisations fully enriched.**

Three options, in order of preference:

1. **Flag it.** Missing ticketing provider or venue size lowers the lead score, or raises an alert. Do not silently pass.
2. **Route it.** Leads missing LinkedIn go into a different outreach campaign that does not use LinkedIn. (Powerful, but only once you are at volume.)
3. **Reject it.** Harder qualification that eliminates leads with missing data points. Use sparingly — you will throw away good leads.

Appic chose option 1 plus a manual review gate. That is the right call when you are starting.

### Deliverable
An enrichment step inside the sourcing skill, with fallback logic and a fill-rate number you report weekly.

---

## PHASE 4 — Data standardisation

**Goal:** every run produces the same columns, in the same order, with the same names.

**Mode: DWY.** The client owns the schema. Only they know which fields their business actually uses.

This phase looks boring. It is the phase that saves the project. Appic spent most of 13 August on it, after inconsistent output made lead prioritisation impossible.

### Steps

**4.1 — Build the master Google Sheet template.**
One sheet. Two tabs:
- **Organisations** tab
- **People** tab

List every required column, in the exact sequence you want it. Freeze the header row. This file is now the contract.

**4.2 — Point the skill at the template.**
Give the skill the sheet as its output specification. Tell it: match this sequence, these names, exactly. Start a fresh chat for this so the old inconsistent output does not pollute it.

**4.3 — Strip out irrelevant data.**
Appic removed columns nobody used. Clutter hides the signal. If a column has not driven a decision in three weeks, delete it.

**4.4 — Agree valid ranges.**
Attendance is the example. Agree a floor and a ceiling. Anything outside is an error, not a lead.

**4.5 — Separate sourcing from writing.**
**This is the critical decision of Phase 4.** On 13 August Appic removed the Pipedrive upload from inside the lead generation skill.

Why: you cannot debug sourcing while it is writing to your CRM. Bad rows become bad records become bad outreach.

New shape:

`Sourcing skill → Google Sheet → HUMAN REVIEW → separate CRM import skill → CRM`

The human review gate stays. Even at maturity. Alex reviews Friday 3pm, uploads after.

### Deliverable
A master sheet template, a sourcing skill that writes only to that sheet, and a separate import skill (Phase 5).

---

## PHASE 5 — CRM import and hygiene

**Goal:** clean records land in the CRM, mapped correctly, with no duplicates.

### 5.1 — Build the import skill
Separate skill. Input: the approved sheet. Output: organisations, contact people, and deals in the right pipeline.

Give it an example sheet in the exact template format, then say:

> Do this for two or three leads only, and populate the data fields as per my requirements.

Test small. Check the field mapping visually in the CRM. Appic found fields landing in the wrong slots on the first runs — a five-minute check catches it.

### 5.2 — Map every field explicitly
Do not trust automatic mapping. Write the map out:

| Sheet column | CRM object | CRM field |
|---|---|---|
| Organisation name | Organization | Name |
| Website | Organization | Website |
| Instagram followers | Organization | Custom field |
| Attendance | Organization | Custom field |
| Ticketing provider | Organization | Custom field |
| Contact name | Person | Name |
| Direct email | Person | Email (work) |
| Phone | Person | Phone |
| Event name + date | Deal | Title / custom field |
| Tier | Deal | Custom field |

Create the custom fields in the CRM by hand first. Then map.

### 5.3 — Duplicate check before write
The skill must check whether the organisation already exists before it creates anything. Enrich the existing record instead of creating a second one.

### 5.4 — Define ownership
Who owns a new deal? Default it to one person. Build in the ability to reassign in bulk later — Appic set all deals to Alex initially, with transfers to Peter or Sophie planned once territory rules were agreed.

### 5.5 — Define pipeline stages with hard rules
**Do this before you automate any deal movement.** This was Aryan's strongest warning on 17 August:

> "Once the system is live, it's going to move deals for you across the pipeline. For that, we need really, really hard rules on when to do that and when not to do that."

For each stage, write the one event that is genuinely true when a deal sits there:

| Stage | Hard rule — what must be true |
|---|---|
| Qualified | *Define this properly.* Most sales organisations mean "we have met them and heard a real buying signal," not "we sourced them." |
| Contacted | An outbound touch has been sent |
| In conversation | They replied |
| Meeting booked | A calendar event exists |
| Proposal sent | **The proposal document was actually sent.** Aryan's own rule: the deal only moves when the PandaDoc goes out. |
| Approved / requirements pending | They said yes; you are waiting on assets |
| Ready to close | Assets received |
| Closed | *Define this.* Appic's definition is post-event — campaign delivered, tickets sold, event finished. |
| Lost | Define the trigger and the timeout |

Two extra rules to agree:
- **Stale rule.** Deals with no activity for 3–6 months get archived or reactivated. Do not delete them.
- **Reactivation.** Use a CRM prospect mining skill on dormant records rather than deleting. Old lost deals are cheaper to reopen than new leads are to source.

### 5.6 — CRM hygiene skill
A recurring job that moves deals based on the hard rules above, using calls, emails and meetings as evidence.

**Do not switch this on until the stage rules are written and signed off.**

### Deliverable
An import skill, a field map, custom fields created, written pipeline stage definitions, a hygiene routine (drafted, not yet live).

---

## PHASE 6 — Reporting and visibility

**Goal:** the numbers arrive without anyone asking for them.

### 6.1 — The daily pipeline report
A scheduled job that reads the CRM pipeline and reports current deal stages.

Configuration questions the skill will ask — have the answers ready:
- Which pipeline?
- Where does the report land? (Slack channel, email, Drive)
- What time? (Appic: 08:30 Amsterdam)
- What is the sales cycle definition?

### 6.2 — The weekly sales cycle report
Which deals moved between stages this period, what came in new, what closed out. Post to Slack.

### 6.3 — Make it HTML and branded
A text report gets ignored. An HTML report gets read.

1. Give the AI the brand guidelines — colours, fonts, logo. Paste them into the chat if there is no brand skill yet.
2. Ask it to render the report as HTML using those brand tokens.
3. **Review the content first, then style it.** Do not brand a report you have not verified. Aryan stopped Alex from finalising the skill before checking the numbers were right.
4. Save the HTML output into the skill as a reference file, so every future run matches.

### 6.4 — Host it so it can be shared
Local HTML files are dead ends. Deploy to **Vercel** (or Netlify) and get a live URL. Then Slack the link.

### 6.5 — The extra reporting skills
Install and adapt these — they exist already, do not build them:
- **Win-loss analysis** — why deals close and why they die
- **CRM prospect mining** — find high-value dormant records worth reopening
- **Call prep** — a brief before every sales call
- **Sales call analyser** — grade the call, extract next steps

### 6.6 — The dashboard (the cockpit)
The single page where the operator lives. This is the control centre for the whole Second Brain.

Requirements gathered on 20 August:
- Must reflect the actual business model. For Appic, revenue is tickets resold, not licence fees — a generic SaaS dashboard is wrong.
- Current data accuracy is good; what is missing is **revenue forecasting** and **decision alerts**.
- It should tell you what to do next, not only what happened.

Ask your provider for dashboard examples before you specify yours. Copy a working shape.

### Deliverable
A daily report, a weekly report, both branded, both hosted, both landing in Slack, plus a dashboard v1.

---

## PHASE 7 — Voice and content

**Goal:** everything the system writes sounds like the client, not like an AI.

**Mode: DWY.** You need their real words. Only they can supply them.

### 7.1 — Build the voice skill
Use a voice-builder skill. Feed it a genuine corpus:
- Sent emails (export from Gmail)
- WhatsApp and Instagram DMs
- Slack messages
- Raw dictated speech (Whisper Flow transcripts work well)
- LinkedIn posts

More is better. Appic's voice skill was calibrated on over 100,000 words of real messages.

**Warning:** this build is token-heavy. Alex's voice-builder chat hit 400,000 tokens. Run it in its own chat, in Code, and `/compact` when needed.

### 7.2 — Add a linter and a judge
A good voice skill has two gates:
1. A **deterministic red-flag linter** — banned phrases, banned structures.
2. A **rubric judge** — scores a draft against the real corpus.

Every draft passes both before it ships. This is what stops the output drifting back to generic.

### 7.3 — Content skills
- **LinkedIn post creator** — weekly post, in the client's voice, on progress and product.
- **Newsletter writer.**
- **Monthly recap deck** — a branded slide deck built from calendar, Drive, CRM and notes. Appic runs this monthly from a brand template so the logo and colours are exact.

### 7.4 — Weekly content rhythm
Draft Monday. Internal review. Post Thursday or Friday. Keep it simple. The point is consistency, not volume.

### Deliverable
A `[name]-voice` skill with linter and judge, plus one content skill in use weekly.

---

## PHASE 8 — Outreach cadence

**Goal:** a defined multichannel sequence, with templated copy, variable personalisation, and fallbacks — ready to automate.

**Mode: DWY.** The client owns the copy. You own the structure. Never write cold copy for a market you do not know.

### 8.1 — Mine what already works
Before designing anything, collect:
- The most successful email exchanges the client has had
- The most successful Instagram and WhatsApp exchanges
- The list of existing clients in the target market, for name-dropping

Feed these to the AI as reference. Correct it when it misidentifies who is a client and who is not. That correction step matters.

### 8.2 — Design the cadence
Appic's shape: **12 touches**, day by day, across four channels plus phone.

Channel order: **Instagram → LinkedIn → Email → WhatsApp**, with **cold calling** inserted.

Example opening (Appic, German festival market):

| Day | Channel | Purpose |
|---|---|---|
| 0 | Instagram DM | Name the next event and date. Note they have no ticketing platform / no app. Ask who the right person is. Get a name. |
| 1 | LinkedIn | Send connection request in parallel |
| 2 | Email | The pitch, ~90 words |
| 3 | LinkedIn DM | "Did the email arrive?" |
| … | Phone | Cold call, cross-referencing every prior touch |

**Cold calling:** check local norms with the client. Alex assumed it was frowned upon in Germany; it is in fact the main sourcing method his whole company uses. Ask, do not assume.

### 8.3 — Cross-reference between steps
This is the technique that makes a sequence work.

> "Hi — we've emailed you, we DM'd you on Instagram, and we connected on LinkedIn recently…"

Each later step names the earlier ones. It converts scattered noise into evident persistence. Build the cross-reference into the copy template, not into the AI's improvisation.

### 8.4 — Templatise the copy, personalise the variables
**The single most important outreach rule in this manual:**

> "It's better to use variables. AI can personalise variables. AI can't personalise full emails. We don't want AI to do that." — Aryan, 18 August

So:
- **Human writes** the message skeleton, once per channel per step.
- **AI fills** the variables.

Variables worth having for an event or venue business:
- `{first_name}`
- `{organisation}`
- `{next_event_name}` and `{next_event_date}`
- `{current_ticketing_provider}`
- `{current_app}` — or the absence of one
- `{instagram_followers}`
- `{secondary_decision_maker_name}`
- `{days_until_event}`

Personalisation hooks that Alex identified as high-response:
- "I see you're using [app X] — here's what that costs you."
- "Your event is in [N] weeks — how are ticket sales tracking?"

These are exactly the checks a human never does at scale and AI does perfectly.

### 8.5 — Build the fallback ladder
Data will be missing. Define the ladder before launch:

| Missing | Fallback |
|---|---|
| No first name | Use organisation name, or the generic greeting |
| No LinkedIn | Skip the LinkedIn steps; add an extra email step |
| No phone | Skip the call; move the WhatsApp step earlier |
| No direct email | **Generic company email.** Every event has one on its website. |
| No Instagram | Start the sequence at email |
| No personalisation hook | Fall back to the event-date hook — that one is always available |

The worst-case message is short and redirect-shaped:

> "Hi — noticed your event is coming up in a few weeks. We help fill remaining capacity at no cost. Who would be the best person to speak to about this?"

Alex's note: do not give more context than that in the fallback. Detail kills the reply.

### 8.6 — Test before launch
Run the cadence against **at least 10 leads with deliberately varied data completeness.** Some with everything. Some with only a generic email. Check that every fallback fires correctly and no message renders with an empty `{variable}`.

### 8.7 — Choose the sending infrastructure
**Lemlist** is the recommended sequencer. It handles email, LinkedIn, WhatsApp and cold-call tasks in one campaign. It has a native connector.

Notes:
- A paid plan is required for real sending.
- **Instagram is not supported.** Handle it as a manual step in the sequence that triggers a **browser automation** — the AI drives a browser and sends the DM. Reliable for 10–30 per day, not for mass sending.
- Build infrastructure that pushes new leads into the Lemlist campaign automatically each week, so nobody uploads a CSV by hand.

### 8.8 — Deliverability
At Appic's volume — 30–50 contacts a week from individual company mailboxes — this is low risk. Still, set the client's expectations:

- Above that volume, **buy a secondary domain** for cold outreach so the primary domain never gets flagged.
- Track deliverability. Most teams, including Appic before this build, track nothing.
- Warm the domain before you scale it.

### Deliverable
A finished cadence table, templated copy per channel per step, a variable list, a fallback ladder, a tested campaign in Lemlist, and an Instagram browser automation.

---

## PHASE 9 — Post-call and CRM automation

**Goal:** the hour after a sales call happens by itself.

### 9.1 — Post-discovery follow-up
Trigger: a call transcript appears in the notetaker.

The skill should:
1. Read the transcript.
2. Extract what the prospect actually needs and what they objected to.
3. Draft the follow-up email in the client's voice (Phase 7).
4. Generate or pre-fill the proposal.
5. Update the CRM record.
6. Move the deal — but only if the hard rule for the next stage is genuinely met.

**Configure it to the client's real sales process.** The setup skill should ask: do you send the proposal right after the first call, or later? The answer changes the whole flow.

**On proposals:** Appic found that in new international markets, lightweight proposals without formal contracts close faster. Do not force a heavy document because that is what the home market does.

### 9.2 — Daily email triage and drafting
A scheduled job that:
1. Reads overnight email.
2. Summarises what arrived.
3. Drafts replies in the client's voice.
4. Leaves everything as a draft for human approval.

**Build self-improvement into it.** When the human edits a draft before sending, that edit is training data. Feed the corrections back into the voice skill.

### 9.3 — Notifications, not dashboards
The system should interrupt the operator only when it matters:
- An important email arrived
- A prospect replied
- A deal has gone quiet past the stale threshold
- The weekly lead sheet is ready

Route these to Slack.

### Deliverable
A post-discovery skill, a daily triage routine, and a notification rule set.

---

## PHASE 10 — Scheduling: local to cloud

**Goal:** the system runs whether or not anyone opens a laptop.

### 10.1 — Start local
Create every routine as a local scheduled task first. Test the output. Fix it.

**Local routine configuration checklist:**
- [ ] Model set to **Opus**, not Haiku. (Alex's first voice routine defaulted to Haiku and produced weak output. Aryan: *"this is set to Haiku, which is just not ideal."*)
- [ ] A working folder is attached — the folder where the relevant context lives
- [ ] Run time set for when the machine is definitely awake
- [ ] Output destination set (Sheet, Slack, Drive)

### 10.2 — The core weekly rhythm
Appic's live schedule:

| When | Job | Output |
|---|---|---|
| Friday 15:00 | Lead generation skill runs | Google Sheet link posted to Slack |
| Friday 15:00–17:00 | **Human review** | Alex edits, corrects, approves |
| Monday morning | CRM import skill runs on the approved sheet | Deals created in Pipedrive |
| Monday | Outreach campaign launches on the new batch | Lemlist sequence starts |
| Daily 08:30 | Pipeline report | Slack |
| Daily overnight | Email triage and drafting | Gmail drafts |
| Weekly | Sales cycle report | Slack, HTML, hosted |

**Keep the human review gate on Friday.** It is not a temporary crutch. It is the quality control that lets everything downstream be automatic.

### 10.3 — Move to the cloud
Once a routine is stable and GitHub access exists, recreate it as a cloud routine (see A4 for the exact prompt).

Sequence: create as **draft** → review the repository and the connector list → activate → monitor the first three runs → report results.

### 10.4 — Audit every routine
Before you hand over, do this — it is the best hour you will spend:

> Open a new chat, attach the Sales OS folder, and ask it to explain every single routine to me: the sequence, the logic behind each one, and why, what and when it runs.

Then correct anything that does not match reality. This takes a lot of back and forth. Budget a half-day. It catches assumptions the AI made silently during setup.

### Deliverable
All routines live, cloud-hosted where possible, documented, and audited line by line.

---

## PHASE 11 — Sales OS assembly

**Goal:** all the parts become one product with one front door.

This is the phase that turns a pile of skills into something you can sell. BenAI packages this as a plugin and sells it at around **£/€10k**.

### 11.1 — What goes in the plugin
A Sales OS plugin bundles:

| Component | Purpose |
|---|---|
| Lead generation skill | Sourcing |
| Enrichment skill | Contact data |
| CRM import skill | Write to CRM |
| CRM hygiene skill | Move deals on hard rules |
| Call prep skill | Brief before every call |
| Sales call analyser | Grade the call, extract actions |
| Win-loss analysis | Why deals close and die |
| Post-discovery follow-up | The hour after the call |
| Voice skill | Everything sounds like them |
| Reporting skills | Daily, weekly, branded, hosted |
| Dashboard builder | The cockpit |
| **The setup interview** | Builds all of the above around their business |

### 11.2 — The setup interview
The plugin should not install blind. It runs an interview. Budget **45–60 minutes** with the client. It:

1. Reads what context and skills already exist.
2. Asks which existing skills are actually used weekly, and which are dead weight.
3. Asks what tools they use, and confirms every connector is live.
4. Asks **how** they use those tools — e.g. *where exactly in Pipedrive does lead information live?*
5. Asks the hard commercial questions:
   - What does a customer actually give you when they say yes?
   - What is that worth? Write the formula.
   - Which stage in your pipeline means what? What must be true for a deal to sit there?
6. Proposes a folder structure and confirms it with the client.
7. Builds the folder structure.
8. Builds the dashboard with their branding.
9. Creates all the scheduled tasks (local first).

Expect the client to say "I need to find this out" on at least two questions. That is the interview doing its job.

### 11.3 — Static and dynamic context
Design the folder structure around the two context types:

```
[Client] Second Brain/
├── Context/                 ← STATIC. Written once, reviewed quarterly.
│   ├── icp.md
│   ├── business-model.md
│   ├── gtm-strategy.md
│   ├── pipeline-stages.md
│   ├── brand.md
│   └── team.md
├── Live/                    ← DYNAMIC. Written by scheduled tasks.
│   ├── pipeline-snapshot.md
│   ├── recent-meetings.md
│   ├── new-leads.md
│   └── inbox-summary.md
├── Skills/
├── Outputs/
│   ├── lead-sheets/
│   └── reports/
└── CLAUDE.md                ← House rules and routing
```

The scheduled tasks exist to keep `Live/` fresh. The dashboard reads both.

### 11.4 — Organise by function, not by project
Fold work into buckets that recur: lead generation, outreach, reporting, conferences, content. Context accumulates inside a bucket and makes every future run better. A folder per one-off project throws that away.

### 11.5 — Where the Sales OS lives
Start it as its **own folder**, separate from the general Second Brain. Merge it in later once it is stable. Keeping it separate during the build stops one broken thing from breaking everything.

### Deliverable
One installed plugin, one completed interview, one folder structure, one dashboard, all routines created.

---

## PHASE 12 — Team rollout

**Goal:** it stops being one person's tool.

### Steps

1. **Pick the pilot group.** Start with the commercial department, not the whole company.
2. **Set permissions and access control.** Who can run which skill. Who can write to the CRM. Who can send outreach.
3. **Make context shared, not personal.** The `Context/` folder is company property. Voice skills are per person.
4. **Assign ownership per skill.** Every skill needs a named owner who reviews its output monthly.
5. **Train on the loop, not the buttons.** Teach them the tightening loop from Phase 2.6. That is the durable skill.
6. **Set the review rhythm.** Weekly: check outputs. Monthly: retire dead skills, tighten live ones.
7. **Expand by department.** The same architecture works for marketing, finance and support. The Sales OS is the template, not the limit.

### Deliverable
A permissions matrix, an owner per skill, a training session, a review calendar.

---

## The parallel module — conference and event prospecting

Not every business needs this. Run it as an add-on where live events matter.

**Purpose:** decide which conferences are worth the money and the days, then mine them for leads.

### The two-step logic
Alex's insight on 17 August, which is the right way to build it:

1. **Qualify the conference first.** The signal is the **speaker list**. If your ICP is on stage, your ICP is in the room. Score the event.
2. **Only then mine the attendees.** Once you have decided to attend and bought the ticket, you get access to the attendee list. Build a second skill for that.

### The qualification skill
Inputs: your ICP, your qualification criteria, and who you would need to meet.
Sources: the event's own programme, speaker, audience and ticketing pages.
Output: a scored table, 1–10, colour-coded. Green = go.

Appic scored ADE, Future Festivals, business-day events and IMS this way and got a usable answer in a handful of prompts.

### Honest scoping
Ask how many conferences the client attends per year. If it is under ten, do not build a heavy automated system. Make it a slash command, run it once a year when planning the calendar, and spend the effort elsewhere.

### The promoter mining play
For a music industry client: at a major event like ADE, the promoter list is public or semi-public. Scrape it, enrich the promoters, and run manual Instagram and email outreach against them. This is one of the highest-quality lead sources available, and it is seasonal.

---

# PART C — THE BUSINESS

## C1. What you are actually selling

You are not selling AI. You are not selling skills. You are selling this:

> **A commercial operating system that sources, qualifies, enriches, contacts, tracks and reports on new business — and that gets better every week because a human corrects it.**

The product has four visible parts. Lead with these on a sales call:

1. **A lead engine** that produces 30–50 qualified prospects a week, automatically, with the client's own qualification rules baked in.
2. **An outreach machine** that runs a 12-touch multichannel cadence in the client's own voice, personalised by real data.
3. **A CRM that maintains itself** — records created, deals moved on hard rules, dormant deals resurfaced.
4. **A cockpit** — one branded page and a Slack feed that tells them what happened and what to do next.

## C2. The three offers

### Offer 1 — Diagnostic
**What:** Phase 0 only. Bottleneck interview, pipeline map, prioritised roadmap, tool audit.
**Time:** One week, two sessions.
**Delivery:** DWY.
**Positioning:** Paid discovery. Credit it against the build if they proceed.
**Why it works:** it removes your risk on scoping and it earns trust before any money is at stake.

### Offer 2 — Build (DFY) + Enablement (DWY)
**What:** The full 12 phases.
**Time:** Four to five weeks, with a **daily 30–45 minute session**.
**Delivery:** Mixed — you build the technical layers, the client owns ICP, schema, copy and stage rules.
**Deliverables:** see C4.
**Why the daily cadence:** it is not a nice-to-have. Momentum is what makes this work. Weekly calls let a blocker sit for six days.

### Offer 3 — Operate (retainer)
**What:** You run it. Weekly tightening loop, monthly skill review, new skills as needs appear, cloud routine monitoring.
**Time:** Ongoing.
**Delivery:** DFY with a monthly report.
**Why they buy it:** the system decays without the tightening loop. That loop is a skill, and most clients will not do it.

### Reference point on pricing
BenAI gates the Sales OS plugin behind a **~£/€10k** sale. Use that as your anchor for the packaged product. The build engagement sits above it. The retainer sits below it, monthly.

## C3. Which mode, which phase

| Phase | Mode | Why |
|---|---|---|
| 0 Discovery | Either | DWY if they are technical, DFY if you want speed |
| 1 Environment | **DFY** | Google Cloud OAuth will lose a commercial buyer |
| 2 Lead engine | DFY build, **DWY tune** | You build. They must run the tightening loop themselves. |
| 3 Enrichment | DFY | Tool plumbing and credit management |
| 4 Data schema | **DWY** | Only they know what fields their business uses |
| 5 CRM import | DFY build, **DWY rules** | Stage definitions must be theirs |
| 6 Reporting | DFY | Needs brand assets from them, nothing more |
| 7 Voice | **DWY** | Needs their real corpus and their judgement on what sounds right |
| 8 Cadence | **DWY** | Never write cold copy for a market you do not know |
| 9 Post-call | DFY | Configure to their process |
| 10 Scheduling | DFY | Technical |
| 11 Sales OS | DFY, guided | The interview is the client's contribution |
| 12 Team rollout | **DWY** | It is a change management job, not a technical one |

**The rule of thumb:** anything requiring their business knowledge is DWY. Anything requiring tooling knowledge is DFY. Never blur the two — a client who did not write their own ICP will not defend the system when it produces a lead they dislike.

## C4. The deliverables list

Put this in the proposal verbatim.

**Documents**
- Bottleneck memo and pipeline map
- ICP document
- Qualification scoring model with weights and tiers
- Master data schema (Google Sheet template)
- CRM field map
- Pipeline stage definitions with hard rules
- Outreach cadence table with copy per step
- Variable list and fallback ladder
- Routine register (what runs, when, why)

**Working systems**
- Configured environment, all connectors live
- Lead generation skill
- Enrichment layer
- CRM import skill
- CRM hygiene skill
- Voice skill with linter and judge
- Content skill (LinkedIn or newsletter)
- Daily pipeline report, branded and hosted
- Weekly sales cycle report, branded and hosted
- Post-discovery follow-up skill
- Daily email triage routine
- Outreach campaign live in the sequencer
- Instagram browser automation (if relevant)
- Dashboard / cockpit
- All routines scheduled, cloud where possible
- The Sales OS plugin installed and configured

**Enablement**
- Daily sessions, recorded
- Homework tracker maintained throughout
- Final routine audit walkthrough
- Team training session
- Permissions matrix and skill ownership map

## C5. Client prerequisites — send this before day one

Blockers in this list cost Appic real days. Get them moving before the engagement starts.

- [ ] **GitHub organisation access.** If they are on GitHub Enterprise, an admin must grant the AI app access. Start this now — it has a lead time and it blocks all cloud automation.
- [ ] **Admin rights** on the CRM to create custom fields.
- [ ] **A Google account** that can create a Google Cloud project and accept the GCP Terms of Service.
- [ ] **Brand assets** — colours, fonts, logo, tone guidance.
- [ ] **Writing corpus** — an export of sent emails and messages for the voice skill.
- [ ] **Budget approved** for: enrichment credits (Lusha), scraping (Apify, Firecrawl), sequencer (Lemlist paid plan), hosting (Vercel).
- [ ] **Existing CRM data export**, so the deduplication rule has something to check against.
- [ ] **A named decision maker** who attends the daily session. Not a delegate.

## C6. Metrics — how you prove it worked

Baseline these in Phase 0. Report them weekly.

| Metric | Why it matters |
|---|---|
| Qualified organisations sourced per week | The engine's output |
| % surviving human review | Skill quality — should rise every week |
| Enrichment fill rate (people with a direct email / phone) | Reachability. Appic's honest starting point: 11 of 19. |
| Duplicate rate against CRM | Should trend to zero |
| Hours of human work per 50 leads | The savings number the CFO wants |
| Touches sent per week | Cadence throughput |
| Reply rate by channel | Which channel earns its place |
| Meetings booked per 100 sourced | The number that pays for the system |
| Deals auto-moved correctly vs corrected | Trust in the hygiene rules |
| Lead gen run duration | Rising = the skill is bloating, split it |

The metric to lead with in the pitch is **hours per 50 leads** for the diagnostic, and **meetings booked per 100 sourced** for the retainer renewal.

## C7. The sales narrative

Structure the pitch in five beats.

**1. The bottleneck.** "Where does your pipeline actually break?" Let them say it. It is almost always sourcing and qualification, and it is almost always unstructured.

**2. The cost of it.** Hours per week times the rate. Plus the deals lost to slow follow-up.

**3. The system.** Walk the chain: source → qualify → enrich → import → outreach → follow-up → report. Point at each link and say what it does by itself.

**4. The proof.** Show a real output sheet. Show a branded report. Show a Slack notification arriving. Do not show a slide of features.

**5. The loop.** Explain the weekly tightening loop. This is the moat. Any competitor can install a tool. Only a system with a correction loop gets better.

**Objections and answers:**

| They say | You say |
|---|---|
| "We already have a CRM." | This fills it and maintains it. Your CRM is the filing cabinet. This is the person who files. |
| "We tried an AI tool and it was generic." | Correct — because it was not personalised. No skill works out of the box. We spend a week on your ICP alone. |
| "Won't AI write bad emails?" | AI never writes your emails. You write the templates. AI fills the variables. That is the rule we build on. |
| "What if the data is wrong?" | There is a human review gate every Friday before anything reaches your CRM. Nothing writes to the CRM unreviewed. |
| "How long until it works?" | Week one you get a lead sheet. Week four the whole loop runs. Month three it is noticeably better than week four, because of the tightening loop. |

## C8. Delivery risks and how to price them

| Risk | Likelihood | Mitigation | Commercial handling |
|---|---|---|---|
| GitHub org access delayed | High | Request on day zero | Local routines as the interim deliverable; do not promise cloud in week one |
| Google Workspace OAuth failure | High | Use the installer skill; one Google account | Bill it inside Phase 1; budget half a day |
| Enrichment fill rate below expectation | Certain | Fallback ladder; set expectations early | Quote fill rate as a range, never a promise |
| Client cannot articulate their ICP | Medium | Interview it out of them over two sessions | Bill discovery separately so this is not scope creep |
| Platform bugs (app resets, question loops) | Medium | Work in Code, not Cowork; `/compact` | Build slack into the timeline |
| Skill bloats past 200k tokens | Medium | Split it | Expect one split per major skill |
| Client will not run the tightening loop | High | Sell the retainer | This is the retainer's whole reason to exist |

## C9. Client onboarding questionnaire

Send this after the diagnostic, before Phase 1.

**Business**
1. What do you sell, in one sentence?
2. What does a customer actually give you when they say yes? Quantities, timing, value.
3. Write the revenue formula for one closed deal.
4. Which markets are you entering next?

**ICP**
5. Geography.
6. Organisation type and size range.
7. Three signals that tell you a prospect is a good fit.
8. Three signals that tell you to walk away.
9. Which of your existing customers is the perfect example? Why?

**Process**
10. List your pipeline stages.
11. For each stage: what must be genuinely true for a deal to sit there?
12. What triggers a deal being marked lost?
13. Who owns new deals? How are they distributed?
14. Do you send a proposal after the first call, or later?

**Outreach**
15. Which channels do you use today? In what order?
16. Paste your three most successful outreach messages.
17. Which existing customers can we name-drop in this market?
18. Is cold calling normal in this market?

**Tools**
19. CRM, and who administers it.
20. Email platform. How many mailboxes for outreach?
21. Meeting notetaker.
22. Sequencing tool, if any.
23. Enrichment and scraping tools, if any.
24. Where does your team live day to day — Slack, Teams, email?

**Data**
25. Export your current CRM organisations so we can build the deduplication rule.
26. Send brand guidelines.
27. Send an export of sent emails for the voice skill.

## C10. Session template — run every day

30–45 minutes. Same shape every time. This is the operating rhythm that produced the whole Appic build.

| Minutes | Segment |
|---|---|
| 0–5 | Review the homework tracker. Tick off what is done. |
| 5–15 | Client shows what they built or ran. Screen share. |
| 15–30 | Work the blocker live, together. |
| 30–40 | Teach one concept. Skills, MCPs, tokens, routines, context — one per session. |
| 40–45 | Set tomorrow's homework. Update the tracker. |

**Record every session.** The transcripts become the client's own SOP library — and yours. This manual exists only because eighteen days of these calls were recorded.

---

# APPENDIX 1 — The build log, day by day

The real chronology. Use it to set client expectations about pace and about mess.

### Day 1 — Mon 3 August: Find the bottleneck
Identified unstructured lead generation and qualification as the primary bottleneck. Agreed the target: a standardised pipeline for scraping, qualifying, enriching and contacting high-intent leads. Noted that informal proposals without formal contracts close faster in new markets. Agreed to target large festival platforms as data sources with measurable qualification criteria. Set the daily review rhythm. Homework: install the lead generation, voice builder and post-discovery skills.

### Day 2 — Tue 4 August: Environment
Weighted five data sources, balancing quality against volume. Noted duplicate-outreach risk and agreed to cross-check against the CRM. Found autonomous scraping too weak on its own — added Firecrawl and Apify. Created a single central project folder. Agreed to move all work from Cowork to Code. Installed skills globally. Started the Google Workspace setup. Agreed a DNC list to stop re-sourcing existing CRM records.

### Day 3 — Wed 5 August: First output, and the Google Cloud wall
First real output: **40–45 leads**. Google Cloud OAuth configuration consumed most of the session. Manual enrichment still required. Agreed to switch the voice-driven scheduled task from Haiku to Opus. First mention of **Lemlist** for multichannel outreach. Homework: enrich the list manually, filter out existing Pipedrive deals, install voice builder, create a daily email triage task.

### Day 4 — Thu 6 August: Reporting and enrichment
Prototyped a daily Pipedrive pipeline report. Uploaded the win-loss analysis skill. Fixed the Lusha connector authentication. Agreed to scrape **multiple decision makers per organisation** to lift contact rate. Agreed to archive Germany-pipeline leads dormant 3–6 months rather than delete them, and to use CRM prospect mining to reactivate. Agreed brand tokens should be embedded in HTML report output. Planned a theory session on skills, plugins, MCPs and CLIs.

### Day 5 — Fri 7 August: Theory day
The foundational session. Set connectors to Always allow after ~100 permission prompts in one run. Covered: what a skill is, the 200k token rule, `/compact`, `/context`, plugins, connectors, APIs, MCPs, the MCP creator, and CLIs. Installed `find-skills` from skills.sh. Agreed the sales report needed HTML branding and hosting on Vercel. Agreed a weekly LinkedIn post rhythm.

### Weekend 8–9 August
Alex kept iterating alone. Aryan available on Slack and WhatsApp. **Weekend support is part of the offer.**

### Day 6 — Mon 10 August: Scale and structure
Ran the skill at 100–200 leads to test performance and deduplication. Set the weekly cadence: lead gen runs **Friday**, outreach starts **Monday**. Agreed to flag missing fields (ticketing provider, venue size) by lowering the lead score rather than dropping the lead. Discussed folder and project structure tied to the Second Brain, and how `CLAUDE.md` and memory work. Declared in `CLAUDE.md` that the Appic Google Workspace CLI must always be used, to stop CLI collisions. Planned an event-monitoring skill and a CRM hygiene skill.

### Day 7 — Tue 11 August: Skills multiply
Built the monthly meetup deck skill. Completed the HTML sales report skill, pending Vercel deployment. Explored the Record Skill feature for capturing workflows from screen recordings. Agreed to limit event batch sizes so the content team is not flooded. Planned Pipedrive-to-Slack notifications for new qualified leads.

### Day 8 — Wed 12 August: Cohort session
Wider group session. Confirmed the direction: an AI-powered commercial operations system targeting the German festival and promoter market. Another cohort member launched a ~400-lead AI-driven campaign — useful proof at a different scale. Agreed to build a ready list of warm prospects for German market entry.

### Day 9 — Thu 13 August: The reset
**The most important session of the build.** Output inconsistency was making lead prioritisation impossible. Decisions taken:
- Break the monolithic skill into modules: event scraping, enrichment, CRM import.
- Build a **master Google Sheet template** with all fields in a fixed sequence.
- **Remove the Pipedrive upload from the lead generation skill.** Run it separately, after human approval.
- Customise Pipedrive fields to match the sourcing output.
- Verify each sourced org against the CRM before import.
- Fix Google Workspace CLI conflicts caused by multiple CLI setups.
- Sharpen tier definitions and use Instagram follower count as a real metric.

### Day 10 — Fri 14 August: The honest numbers
Tightened criteria produced **20 leads** in the weekly run, against a 20–50 target. Enrichment reality: **11 of 19 organisations fully enriched.** GitHub account creation blocked cloud deployment — fell back to local scheduled tasks. Agreed the Friday-run, Slack-notify, Monday-import rhythm. Turned to conference sourcing, with ADE as the focus and data-driven event scoring. Assigned Lusha credit monitoring.

### Weekend 15–16 August
Short check-ins. Independent work.

### Day 11 — Mon 17 August: Sales OS arrives
Aryan shipped the updated lead gen skill — 33 reference files, Python scripts, sub-agents. Introduced the **Sales OS plugin**: all sales skills bundled, plus a setup interview, folder structure, dashboard and scheduled tasks. Confirmed the plugin is a gated ~10k product. Agreed the conference skill should qualify events by speaker list first. Deprioritised Instagram prospecting — the German go-to-market targets larger tier-one events. Worked through pipeline stage definitions and the need for hard rules before automating deal movement. Assigned the outreach cadence as homework.

### Day 12 — Tue 18 August: The cadence
Lead gen skill accepted as good enough, with known gaps in contact data. Conference qualification skill built and scored — then correctly judged not worth heavy automation at six events a year. Presented the **12-touch cadence** across Instagram, LinkedIn, email and WhatsApp. Added **cold calling** after confirming it is standard in the German market. Agreed the variable-personalisation rule and the fallback ladder. Created the Lemlist account and connected it. Confirmed Instagram needs browser automation. Attempted the local-to-cloud routine conversion and discovered the feature had been removed — a fresh cloud routine is required. Agreed to audit every Sales OS routine by asking the AI to explain each one.

### Day 13 — Wed 19 August
Short cohort check-in.

### Day 14 — Thu 20 August: Ready to launch
Cadence near final, with fallbacks and a secondary decision maker for personalisation. Agreed to test the cadence on **10 leads with varying data completeness** before launch. Agreed to add phone-call reminders for timing. Planned the Lemlist upload and campaign launch for the following Monday. GitHub Enterprise organisation access identified as the blocker for cloud routines — admin request raised. Sales dashboard confirmed accurate but missing revenue forecasting and decision alerts; a dashboard-creator skill agreed. Lemlist walkthrough scheduled for the next session.

**Where the build stands at the end of the log:** the sourcing and data layers are working and reviewed weekly. The CRM layer is live with human approval. The outreach layer is built and about to launch. The cloud layer is blocked on one admin permission. The dashboard is v1 and needs forecasting.

That is a realistic picture of week three. Show it to clients. It sets honest expectations far better than a finished-looking diagram.

---

# APPENDIX 2 — Pitfalls register

Every one of these actually happened. Give this list to your delivery team.

| # | Pitfall | Symptom | Fix |
|---|---|---|---|
| 1 | Connectors on "needs approval" | 50–100 popups in one run | Always allow, per connector |
| 2 | Wrong model on a routine | Weak, shallow output | Set the model to Opus, not Haiku |
| 3 | No folder attached to a routine | It cannot see any context | Attach the working folder in the routine editor |
| 4 | Local routine, laptop asleep | Silent no-run | Set the time for waking hours, or move to cloud |
| 5 | Cannot convert local routine to cloud | The feature no longer exists | Create the cloud routine fresh |
| 6 | GitHub org access not granted | All cloud routines blocked | Request on day zero; stay local meanwhile |
| 7 | Multiple Google accounts in browser | OAuth attaches to the wrong account | Sign out of all but one |
| 8 | Multiple Workspace CLIs on one machine | Authentication conflicts | One CLI; declare it in `CLAUDE.md` |
| 9 | Sourcing skill writes straight to CRM | Bad data becomes bad records | Split sourcing from import; insert human review |
| 10 | Inconsistent output columns | Cannot prioritise leads | Master Sheet template as a fixed contract |
| 11 | Unbounded data sources | Chaotic, slow, low-quality results | Limit to 4–6 weighted sources |
| 12 | Skill grows past 200k tokens | Quality degrades quietly | Split it into modules |
| 13 | Chat over 400k tokens | Model gets forgetful | `/compact` |
| 14 | Too many MCPs loaded | 36k+ tokens consumed before you start | Convert to CLIs |
| 15 | Running a skill without context | Generic, wrong output | Read the skill; supply context first |
| 16 | Building a skill for a yearly task | Wasted days | Make it a slash command; move on |
| 17 | Fields landing in the wrong CRM slots | Silent data corruption | Test on 2–3 records; check visually |
| 18 | Duplicate organisations created | Same prospect contacted twice | Check the CRM before write; maintain a DNC list |
| 19 | Expecting 100% enrichment | Disappointment and rework | Fallback ladder; report fill rate honestly |
| 20 | AI writing full emails | Generic outreach, damaged brand | Human writes templates; AI fills variables only |
| 21 | Automating deal movement before rules exist | Pipeline becomes fiction | Write hard rules per stage first |
| 22 | Branding a report before verifying it | A beautiful, wrong report | Verify content, then style |
| 23 | Cowork bugs — resets, repeated questions | Lost work and time | Work in Code |
| 24 | Assuming a market's norms | Cold calling wrongly ruled out | Ask the client about local practice |
| 25 | Cold sending from the primary domain at volume | Domain reputation damage | Secondary domain above ~50/week; warm it |
| 26 | Enrichment credits burned silently | Sudden dead stop mid-run | Assign a named credit owner; monitor weekly |

---

# APPENDIX 3 — Prompt library

Copy these. They are the exact prompts that worked.

**Tighten qualification criteria**
> Go through every lead in this sheet. Mark whether it is a high-value prospect or not, and add a column with the exact reason why, so the qualification rules get more stringent on the next batch. Here are my current qualification rules: [paste]. Research any missing Instagram handles and include the follower count.

**Create a skill from a completed process**
> We have just walked through this entire process together. Create a skill out of it using the skill-creator skill. Include the reference files it needs.

**Replace a skill with an updated version**
> Save a copy of my current [Skill Name] to my downloads folder first. Then replace my current version of [Skill Name] with the one in the downloads folder, across all of its copies on my machine.

**Convert a local routine to a cloud routine**
> Check out my [routine name] local routine. I want to convert it into a cloud-based routine. Create a new GitHub repository to work inside. The skill it needs is [Skill Name] — find the most updated version and add it to the repository. Work out every connector the skill needs as a prerequisite and add those too. Do not turn it on yet — keep it as a draft and tell me when it is done.

**Audit the routines**
> Explain every single routine in this folder to me: the sequence, the logic behind each one, and why, what and when it runs. Go one at a time. I will correct anything that does not match how we actually work.

**Test the CRM import safely**
> Here is an example lead list in our standard template. Do the import for two or three leads only, and populate the data fields exactly as specified in the field map. Show me what you created before doing any more.

**Build the outreach cadence**
> Here are our most successful email, Instagram and WhatsApp exchanges, and here is our list of existing clients in this market. Draft a complete outreach cadence of 12 touches, day by day, in this channel order: Instagram, LinkedIn, email, WhatsApp, with cold calling included. Each step must cross-reference the previous steps. Give me a table with day, channel, purpose, and the exact copy with variables marked.

**Check your token position**
> /context

**Compress a long chat**
> /compact

**Find a skill mid-task**
> Find me a skill that will help me [task].

---

# APPENDIX 4 — The one-page summary

Print this. It is the whole manual.

**The chain:** Source → Qualify → Enrich → Standardise → Import → Outreach → Follow-up → Report → Improve.

**The rules:**
1. Never run a skill without context.
2. Walk the process manually, then make the skill.
3. Split at 200,000 tokens.
4. Do not automate a yearly task.
5. Perfect the data before you automate the write.
6. Human writes templates; AI fills variables.
7. Hard rules before automated deal movement.
8. A human review gate stays, forever.
9. Local first, cloud second.
10. Daily sessions. Recorded. Momentum is the product.

**The loop that makes it a business:**
Run → Review every row → Write the exact reason for each reject → Feed the reasons back → Tighten the skill → Run again.

**The sell:** they can buy tools anywhere. They cannot buy the loop.

---

*Built from 18 recorded working sessions, 3–20 August 2026. Alex van Krimpen (Appic) and Aryan Dua (BenAI).*
