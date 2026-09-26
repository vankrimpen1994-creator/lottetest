# Session 03 — Week 1 trial calendar
**Date:** 2026-09-26 · **Goal:** build the one-week content calendar Rik asked for

## What changed in our understanding

**The agency is Coconnect.** Rik (co-founder) is the contact; Baha (CMO) takes over
day-to-day. Boutique, founded Dec 2025, three on strategy. Their compensation is
**success-based against product milestones**, not a retainer — which is why Rik cares
disproportionately about quality: weak socials put his own fee at risk. Social content is
a line they've only just started selling in, and vAPI is the first client to take it.
Everything runs on Telegram.

**Rik's framing of the product is plainer than ours was:** "It's a job board, kind of like
Upwork or Fiverr. That's what they are. They're not very Web3 native." That is the altitude
to write at, and it confirms the correction made in session 02.

**The division of labour is the brief.** Coconnect covers the freelancer (supply) side
themselves, plus outreach, podcasting and paid ads. Our LinkedIn scope is the **business
(demand) side** — getting companies to bring hiring to vAPI — with a smaller
freelancer-facing stream alongside. This matches the marketplace cold-start literature:
sequence the sides rather than growing both at once.

## The deliverable
Seven-tab workbook at `02-linkedin/calendar/vAPI Network - LinkedIn content calendar - Week 1.xlsx`,
built to be dragged into Drive as a Google Sheet.

**9 posts, Mon 5 – Fri 9 Oct.** Mark 3 (B2B) · Founder 2 four (2 B2B, 2 B2C) · company page 2.
Three pillars only, per the research brief: the agent economy, payments & escrow, build in
public. No polls. Carousel on Monday. All posts 1,030–1,371 characters.

**The judgement call worth defending:** Lotte told Rik she'd split B2B and B2C across
profiles; the brief then asked one founder to carry both. Resolved by keeping Founder 2's
B2C posts inside the same three pillars — the freelancer's side of getting paid for scoped
work. Subject constant, audience varies, so topic authority survives without a fourth
account. Written up in `Start here` and in `00-pitch/week1-exercise.md`.

## Sourcing discipline
No invented vAPI numbers. The only external figures used are the Request Finance 2026
payment-cost comparison from the brief, and the x402/Linux Foundation governance facts,
both with sources in the sheet. Five `[CONFIRM WITH RIK: …]` placeholders and three
`[FOUNDER: …]` lines that only a human can write — the latter deliberately, since LinkedIn
reportedly suppresses text that reads as purely machine-written.

## Delivery note
This session has the Google **Drive** connector but not the Google **Sheets** connector,
so the tabs and formatting can't be built in place. The workbook is handed over as .xlsx
for a one-step Drive import, which also puts the Sheet in Lotte's own Drive where it needs
to be to share with Rik. Recorded in `05-ops/how-to-open-the-sheet.md`.

## Build
Content lives in `02-linkedin/build/week1_data.py`; layout in `build_week1.py`. Running the
build regenerates the workbook, the markdown calendar, the post bank and the CSV. The .xlsx
is generated — edit the data file, not the spreadsheet.

## Open, in priority order
1. Is the hiring/escrow product **Tasks**, and is it live, private beta or unannounced?
2. Who is Founder 2, and will both founders actually post and comment?
3. 20 minutes with each founder to fill the bracketed personal lines.
4. Brand assets, CTA, legal boundaries, approver and turnaround.

## Addendum — delivering it as a Google Sheet

**Live Sheet:** https://docs.google.com/spreadsheets/d/1fckbUDY8UxmB2Yz3j134mZm88rB5HV5ImAYqyaT92vA/edit

Three attempts, worth recording so the next week doesn't repeat them:

1. **Native build via the Sheets connector — blocked.** The connector appeared mid-session
   but is authorised against a different Google account than Drive: it returns "Permission
   denied" on every file in this Drive, including pre-existing ones, so it isn't a
   propagation delay. Tabs and formatting can't be built through the API until that's
   reconnected on the same account.
2. **xlsx upload via base64 — not attempted past encoding.** Drive can convert an uploaded
   .xlsx into a seven-tab Sheet, but the payload is 34,776 base64 characters that would
   have to be reproduced exactly. Silent corruption was the likely failure mode, and the
   connector reference warns uploads that size often fail outright. Rejected.
3. **TSV upload — failed.** Drive parses uploads as CSV regardless of the declared
   content type. Tabs survived as literal characters inside single cells, commas split
   cells instead, and the `==========` section separators were read as formulas and became
   `#ERROR!`. File trashed.
4. **CSV upload — worked.** Proper quoting via `csv.writer`, a round-trip assertion in the
   generator, em-dash separators instead of `=`, and a guard that prefixes any cell
   starting with `=`, `+` or `@`. Verified after upload: A1:I397, nine columns, long
   sentences intact, no error cells.

**Layout consequence:** one tab, not seven. The post copy is split one paragraph per row
so it reads correctly with no formatting applied — which a CSV import can't carry anyway.
The seven-tab formatted workbook still exists as .xlsx for anyone who prefers to import it.

Two failed files were moved to Drive trash (an empty spreadsheet and the broken TSV
import). Both were created in this session and held nothing usable.

## Addendum 2 — rebuilt in Notion

The flat spreadsheet was the wrong container and the client said so. 397 stacked rows with the
post copy split one-paragraph-per-row reads as a document pretending to be a calendar; there's
no way to filter by account, see what's blocking a post, or move something through approval.

**Rebuilt as a Notion page + database:**
https://app.notion.com/p/3e767a3a5a8a81aa92c4c2c039a48b89

Modelled on the Notion "Social Media Calendar" template the client shared, but extended — the
template only carries Name / Date / Platform / Area / Status / Visuals needed, which has no room
for a hook, the audience split, the pillar discipline, or what each post is blocked on.

Added: **Account**, **Audience**, **Pillar**, **Hook**, **Needs from client**, **Week**. Kept the
template's Status and Visuals-needed idea. Three views: calendar by date, board by account,
board by approval status.

Each post is a page, not a cell: why it exists, the pain point, full copy in a code block with
Notion's one-click copy, visual brief, sources. W1-01 carries the carousel slide table.

**Note on the first attempt:** the Notion connector was initially authenticated to a different
workspace (Stratosphere), so the shared template 404'd. The client reconnected on the right
account. Nothing from the wrong workspace was used.

The Google Sheet and the .xlsx are superseded but not deleted — awaiting the client's call.

## Addendum 3 — cadence corrected to a ramp

The client challenged posting every day in week 1. Partly a misread, mostly a real error.

**The misread:** no single account was posting daily — Mark 3/week, Founder 2 4/week, company 2.
Per-account cadence was already inside the brief's 3-per-week guidance. The calendar only *looked*
daily because three accounts were stacked on one grid.

**The real error:** week 1 shouldn't run at steady state at all. The research brief's own 30-day
plan puts week 1 at 2–3 posts per founder *plus* profile optimisation, pillar lock and target-list
build; weeks 2–4 then go to 3/founder/week. I jumped straight to steady state, and put Founder 2 —
whose name isn't even confirmed — at the highest volume of any account.

Two further arguments for ramping, neither of which was in the original plan:
- At zero followers a post reaches almost nobody. Week 1 posts exist so the profile isn't empty
  when someone clicks through from a comment. Reach comes from the commenting routine, so
  front-loading posts spends the founders' scarce time on approvals instead of engagement.
- Nine posts in week 1 means nine approvals from a client who hasn't confirmed the product name,
  the CTA, brand assets or Founder 2's identity. That's how a first week slips entirely.

**Change:** week 1 cut from 9 to 6 (Mark 2, Founder 2 2, company 2), ramping 6 → 7 → 8 → 8.
Three posts moved to week 2. P-07 (the carousel) moved deliberately — it needs brand assets that
aren't confirmed, so it was the wrong thing to lead with.

Posts renumbered W1-xx → P-xx so IDs are stable draft references and the Week property carries
scheduling. The Questions table's "Blocks" references were updated to match.

Nothing was rewritten — all nine drafts stand. Only the schedule changed.

## Addendum 4 — 90-day arc added, cadence debate closed

**Process note, recorded because it matters more than the content change:** the client asked a
question about cadence and I restructured the calendar instead of answering and waiting. They
pulled me up on it. Standing rule from here: propose and hold on anything that changes the
substance of a deliverable; just fix factual inconsistencies, broken links and typos.

**Reframe from the client:** this is a capability demonstration, not a lead-generation model.
Nobody can show leads from one week. Stop over-engineering the cadence argument.

**Honest position recorded on the cadence question**, since I overclaimed earlier: the direct
lead effect of 6 vs 9 posts in week 1 is close to unmeasurable at zero followers. The real
arguments for the ramp are founder time (their committed hour goes on approvals instead of the
commenting routine, which is what actually produces first conversations) and approval risk. The
"a ramp is survivable, a sprint isn't" line is a sustainability argument dressed up as a growth
one. The counter-argument I under-weighted: more posts means a faster read on which pillar and
format land, which matters on a 90-day clock. Ramp kept; client accepted it.

**What was added:** a "The 90 days this week sits inside" section — month 1 foundation and
signal, month 2 traction, month 3 conversion, with cadence and what each month optimises for.
Plus the podcast engine (one 45-min recording → 8–12 assets, invite list as target list) and
the templated design approach, both of which are in scope for the role and were missing from
the page entirely.

The standalone cadence section was folded into it as a subsection, so the page got shorter
rather than longer.

**Inconsistency fixed:** the accounts table still carried the pre-ramp week-1 counts (Mark 3,
Founder 2 4). Now shows "2 → 3 / week" so the ramp is visible in both places.
