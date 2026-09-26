# Getting the calendar into Google Sheets

The calendar is built as `02-linkedin/calendar/vAPI Network - LinkedIn content calendar - Week 1.xlsx`
— seven tabs, colour-coded, with column widths, wrapped text and frozen headers already set.

## Turning it into a Google Sheet (about five seconds)
1. Open Google Drive and **drag the .xlsx in** — or File → Import inside Sheets.
2. Drive converts it automatically. All seven tabs, the colour coding and the formatting
   carry over.
3. Share → anyone with the link can **comment**. Send Rik that link.

Comment access rather than edit: his feedback stays visible as comments instead of
silently changing the calendar.

## Why it's handed over this way
This session has the Google **Drive** connector but not the Google **Sheets** connector,
so Claude can create files in Drive but can't build or edit a Sheet's tabs and formatting
in place. Importing by hand takes seconds and has a second advantage: the Sheet lands in
**Lotte's own Drive**, which is where it needs to live to be shared with Rik.

If you'd rather Claude create and maintain the Sheet directly in future weeks, turn on the
Google Sheets connector for this chat. Claude can then build it, and edit the same file
each week so the link never changes.

## Rebuilding it
The workbook is generated, not hand-made. Content lives in
`02-linkedin/build/week1_data.py`; the layout is in `build_week1.py`.

```bash
cd vapi-network/02-linkedin/build
python3 build_week1.py "../calendar/vAPI Network - LinkedIn content calendar - Week 1.xlsx"
```

That also regenerates the markdown calendar, the full post bank and the CSV. Edit the
data file, never the .xlsx — a hand edit gets overwritten on the next build.
