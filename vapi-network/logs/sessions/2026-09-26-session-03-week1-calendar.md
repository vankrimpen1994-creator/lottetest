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
