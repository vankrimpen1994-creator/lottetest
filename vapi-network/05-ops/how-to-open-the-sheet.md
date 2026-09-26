# The Week 1 calendar in Google Sheets

**Live Google Sheet:**
https://docs.google.com/spreadsheets/d/1fckbUDY8UxmB2Yz3j134mZm88rB5HV5ImAYqyaT92vA/edit

Created in the connected Drive (vankrimpen1994@gmail.com). One tab, 397 rows, nine columns.

## Before sending it to Rik
1. **Share → anyone with the link can _comment_.** Comment access, not edit — his feedback
   stays visible as comments instead of silently changing the calendar.
2. Optional two-minute polish, worth doing: select all → **Format → Wrapping → Clip**
   (keeps rows short), widen column A, and bold the ALL-CAPS section headers. The content
   is correct without it.

## How the one tab is laid out
Scroll straight down. Sections are separated by blank rows and `———  HEADINGS  ———`:

| Section | What |
|---|---|
| Top block | The goal, the three accounts, the three pillars, the B2B/B2C judgement call, what the square brackets mean |
| `THE CALENDAR` | The grid — 9 posts, one row each, with date, account, audience, pillar, format, status and hook |
| `POST COPY` | All nine posts in full, **one paragraph per row** so nothing depends on cell wrapping |
| `MONDAY'S CAROUSEL` | Slide-by-slide copy and design notes |
| `DAILY ENGAGEMENT` | The commenting routine and who to target |
| `MEASUREMENT` | What we track, with honest benchmarks |
| `QUESTIONS FOR RIK` | Nine items to confirm, ordered by what blocks most |

## Why one tab and not seven

The Google **Sheets** connector in this session is authorised against a different Google
account than the **Drive** connector — it can't read any file in this Drive, so tabs and
formatting can't be built through the API. Drive can only create a Sheet by uploading a
file, and it parses any upload as CSV, which is inherently single-tab.

The post copy is therefore split one paragraph per row rather than stuffed into single
tall cells, so it reads properly with no formatting applied at all.

**If you'd rather have the seven-tab formatted version:** drag
`02-linkedin/calendar/vAPI Network - LinkedIn content calendar - Week 1.xlsx` into Drive.
It converts on import with colour coding, column widths and frozen headers intact, and it
lands in your own Drive. Same content, both built from the same source.

**To have Claude build and edit the Sheet directly in future weeks:** reconnect the Google
Sheets connector on the same account as Drive. Then the tabs, colours and formatting can be
built through the API and the link stays the same each week.

## Rebuilding
Content lives in `02-linkedin/build/week1_data.py`. Two builders read it:

```bash
cd vapi-network/02-linkedin/build
python3 build_week1.py "../calendar/vAPI Network - LinkedIn content calendar - Week 1.xlsx"   # 7-tab workbook
python3 to_csv.py                                                                              # flat CSV for Drive upload
```

`to_csv.py` round-trip-checks its own output and guards any cell Sheets would read as a
formula. Edit the data file, never the generated outputs.

## Two files were trashed during this
Two failed upload attempts (an empty spreadsheet, and a TSV import that Drive parsed as
CSV so every tab character stayed literal and the `====` separators became `#ERROR!`).
Both were mine, both empty of usable content, both moved to Drive trash.
