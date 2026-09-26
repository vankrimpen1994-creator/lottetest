# -*- coding: utf-8 -*-
"""Builds the Week 1 deliverables from week1_data.py:
   calendar .md, posts .md, calendar .csv, and the .xlsx uploaded as a Google Sheet."""
import csv, os, sys, textwrap
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from week1_data import WEEK, ACCOUNTS, PILLARS, POSTS

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

ROOT = "/home/user/lottetest/vapi-network"
OUT_XLSX = sys.argv[1] if len(sys.argv) > 1 else "/tmp/vapi-week1.xlsx"

INK      = "1F2933"
HDR_FILL = PatternFill("solid", fgColor=INK)
HDR_FONT = Font(bold=True, color="FFFFFF", size=11)
B2B_FILL = PatternFill("solid", fgColor="E3EEFB")
B2C_FILL = PatternFill("solid", fgColor="FBEFE3")
TITLE_F  = Font(bold=True, size=16, color=INK)
SUB_F    = Font(bold=True, size=12, color=INK)
WRAP     = Alignment(wrap_text=True, vertical="top")
TOP      = Alignment(vertical="top")
THIN     = Side(style="thin", color="C7CDD4")
BOX      = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

def acct(p):  return ACCOUNTS[p["account"]]["name"]
def style_header(ws, row, ncols):
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.fill, cell.font, cell.border = HDR_FILL, HDR_FONT, BOX
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    ws.row_dimensions[row].height = 30

def widths(ws, spec):
    for col, w in spec.items():
        ws.column_dimensions[col].width = w

wb = Workbook()

# ------------------------------------------------------------ 1. Start here
ws = wb.active; ws.title = "Start here"
rows = [
    ("vAPI Network — LinkedIn content calendar", ""),
    (f"{WEEK['label']}: Monday {WEEK['start']} – Friday {WEEK['end']}", ""),
    ("Prepared by Lotte for Coconnect (Rik) — first-draft trial calendar", ""),
    ("", ""),
    ("THE GOAL", ""),
    ("Give the brand a voice it doesn't have yet, and point it at one job: getting businesses to bring their hiring to vAPI Network.", ""),
    ("Coconnect is covering the freelancer (supply) side. LinkedIn's job here is the demand side — with a small, deliberate freelancer stream so the two sides can see each other.", ""),
    ("", ""),
    ("HOW THE THREE ACCOUNTS ARE USED", ""),
    ("Account", "Job"),
]
for k in ("mark", "founder2", "company"):
    rows.append((ACCOUNTS[k]["name"], ACCOUNTS[k]["role"]))
rows += [
    ("", ""),
    ("Why the founders carry it: across a 2026 study of company pages vs. personal profiles, personal profiles averaged 2.6% engagement against 1.6%, and 237% more comments per post. The company page builds credibility; the founders build reach.", ""),
    ("", ""),
    ("THE THREE CONTENT PILLARS — every post is exactly one of these", ""),
    ("1. " + PILLARS[1], "What changes when software buys and commissions work. Who is liable, how trust works."),
    ("2. " + PILLARS[2], "Why agents need a payment layer, why escrow, why digital dollars as the rail."),
    ("3. " + PILLARS[3], "Pre-launch updates, decisions, mistakes and lessons from the founders."),
    ("Only three, on purpose: LinkedIn's ranking model weighs whether an account has earned the right to talk about a topic. An account that posts widely can't be classified, so it isn't shown.", ""),
    ("", ""),
    ("THE B2B / B2C QUESTION — the one judgement call worth flagging", ""),
    ("Rik asked whether to split B2B and B2C across separate profiles. Splitting is cleaner for topic authority, and that was my instinct on the call.", ""),
    ("What I've done instead, and why: Founder 2 carries both, but the B2C posts stay inside the same three pillars — the freelancer's side of getting paid for scoped work. The subject never changes, only who is being addressed. Topic authority survives; we don't need a fourth account nobody has time to run.", ""),
    ("If the freelancer side ever needs real volume, that's the moment to split it onto its own profile. It doesn't need it at 2 posts a week.", ""),
    ("", ""),
    ("WEEK 1 AT A GLANCE", ""),
]
for r in rows:
    ws.append(list(r))
start_counts = ws.max_row + 1
ws.append(["Posts this week", "=COUNTA('Week 1 calendar'!A4:A200)"])
ws.append(["From Mark [Founder 1]", "=COUNTIF('Week 1 calendar'!D4:D200,\"Mark*\")"])
ws.append(["From [Founder 2]", "=COUNTIF('Week 1 calendar'!D4:D200,\"*FOUNDER 2*\")"])
ws.append(["From the company page", "=COUNTIF('Week 1 calendar'!D4:D200,\"vAPI Network*\")"])
ws.append(["B2B posts", "=COUNTIF('Week 1 calendar'!E4:E200,\"B2B\")"])
ws.append(["B2C posts", "=COUNTIF('Week 1 calendar'!E4:E200,\"B2C\")"])
ws.append([])
ws.append(["HOW TO READ THE TABS", ""])
for a, b in [
    ("Week 1 calendar", "The grid. One row per post. Blue rows are B2B, orange rows are B2C."),
    ("Post copy", "The full text of all nine posts, ready to paste. Nothing else needed to publish."),
    ("Carousel — Monday", "Slide-by-slide copy for the week's one carousel."),
    ("Daily engagement", "The commenting routine. This is half the work and the half that usually gets skipped."),
    ("Measurement", "What we track from day one, and realistic benchmarks."),
    ("Questions for Rik", "What I need confirmed before anything publishes."),
]:
    ws.append([a, b])
ws.append([])
ws.append(["ANYTHING IN [SQUARE BRACKETS] IS A DELIBERATE GAP", ""])
ws.append(["Two kinds. [CONFIRM WITH RIK: …] means a fact I won't publish unguessed. [FOUNDER 2: …] / [MARK: …] means a line only the founder can write — a real number, a real opinion. LinkedIn's model penalises text that reads as purely machine-written, so those gaps are load-bearing, not laziness.", ""])
ws.append([])
ws.append(["NOTE ON DATES", WEEK["note"]])

ws["A1"].font = TITLE_F; ws["A2"].font = SUB_F
for r in range(1, ws.max_row + 1):
    v = ws.cell(row=r, column=1).value
    if isinstance(v, str) and (v.isupper() and len(v) > 4):
        ws.cell(row=r, column=1).font = SUB_F
    ws.cell(row=r, column=1).alignment = WRAP
    ws.cell(row=r, column=2).alignment = WRAP
for r in range(start_counts, start_counts + 6):
    ws.cell(row=r, column=1).font = Font(bold=True, color=INK)
widths(ws, {"A": 62, "B": 86})
ws.freeze_panes = "A4"

# ------------------------------------------------------------ 2. Calendar
ws = wb.create_sheet("Week 1 calendar")
ws["A1"] = f"Week 1 — Monday {WEEK['start']} to Friday {WEEK['end']}   ·   9 posts   ·   blue = B2B, orange = B2C"
ws["A1"].font = TITLE_F
cols = ["Date", "Day", "Time (CET)", "Account", "Audience", "Pillar", "Format",
        "Hook — the first line that has to earn the click", "Audience pain point",
        "Call to action", "Visual brief", "Why this post", "Status"]
ws.append([]); ws.append(cols)
style_header(ws, 3, len(cols))
for p in POSTS:
    ws.append([p["date"], p["day"], p["time"], acct(p), p["audience"],
               f'{p["pillar"]}. {PILLARS[p["pillar"]]}', p["fmt"], p["hook"],
               p["pain"], p["cta"], p["visual"], p["why"], "Draft — for review"])
for r in range(4, ws.max_row + 1):
    fill = B2C_FILL if ws.cell(row=r, column=5).value == "B2C" else B2B_FILL
    for c in range(1, len(cols) + 1):
        cell = ws.cell(row=r, column=c)
        cell.alignment = WRAP; cell.border = BOX; cell.fill = fill
    ws.cell(row=r, column=4).font = Font(bold=True, color=INK)
    ws.row_dimensions[r].height = 118
widths(ws, {"A": 12, "B": 11, "C": 11, "D": 22, "E": 10, "F": 20, "G": 22,
            "H": 46, "I": 34, "J": 32, "K": 42, "L": 54, "M": 18})
ws.freeze_panes = "D4"

# ------------------------------------------------------------ 3. Post copy
ws = wb.create_sheet("Post copy")
ws["A1"] = "Full post copy — ready to paste. Square brackets are deliberate gaps; see 'Start here'."
ws["A1"].font = TITLE_F
ws.append([]); ws.append(["#", "When", "Account", "Audience", "Pillar", "Format",
                          "POST TEXT — paste this", "Visual brief", "Sources / fact-check", "Characters"])
style_header(ws, 3, 10)
r = 4
for p in POSTS:
    ws.cell(row=r, column=1, value=p["id"])
    ws.cell(row=r, column=2, value=f'{p["day"]} {p["date"][-5:]}\n{p["time"]}')
    ws.cell(row=r, column=3, value=acct(p))
    ws.cell(row=r, column=4, value=p["audience"])
    ws.cell(row=r, column=5, value=f'{p["pillar"]}. {PILLARS[p["pillar"]]}')
    ws.cell(row=r, column=6, value=p["fmt"])
    ws.cell(row=r, column=7, value=p["body"])
    ws.cell(row=r, column=8, value=p["visual"])
    ws.cell(row=r, column=9, value=p["sources"])
    ws.cell(row=r, column=10, value=f'=LEN(G{r})')
    fill = B2C_FILL if p["audience"] == "B2C" else B2B_FILL
    for c in range(1, 11):
        ws.cell(row=r, column=c).alignment = WRAP
        ws.cell(row=r, column=c).border = BOX
        ws.cell(row=r, column=c).fill = fill
    ws.cell(row=r, column=3).font = Font(bold=True, color=INK)
    ws.cell(row=r, column=7).font = Font(size=11)
    ws.row_dimensions[r].height = 330
    r += 1
widths(ws, {"A": 8, "B": 14, "C": 20, "D": 10, "E": 20, "F": 20,
            "G": 96, "H": 38, "I": 34, "J": 11})
ws.freeze_panes = "C4"

# ------------------------------------------------------------ 4. Carousel
ws = wb.create_sheet("Carousel — Monday")
car = [p for p in POSTS if p.get("carousel")][0]
ws["A1"] = "Monday's carousel — slide-by-slide"; ws["A1"].font = TITLE_F
ws["A2"] = ("10 slides, 1080x1350, exported as a PDF (LinkedIn's document format). "
            "One idea per slide, very large type, legible at thumbnail size. "
            "'vAPI Network' watermark bottom-left on every slide.")
ws["A2"].alignment = WRAP
ws.append([]); ws.append(["Slide", "Headline", "Body copy", "Design note"])
style_header(ws, 4, 4)
notes = {
    "1 — Cover": "Biggest type in the deck. No logo lockup — the watermark is enough.",
    "3": "Source line: 'Source: Request Finance, 2026' in 9pt at the bottom.",
    "4": "Same source line.", "5": "Same source line.", "6": "Same source line.",
    "7": "This is the screenshot slide. Make the 5% dominant.",
    "8": "Same source line. Switch to the accent colour here — the deck turns positive.",
    "9": "The most important slide. Don't crowd it.",
    "10 — CTA": "Clean end card. Confirm the CTA with Rik before export.",
}
for slide, head, body in car["carousel"]:
    ws.append([slide, head, body, notes.get(slide, "")])
for r in range(5, ws.max_row + 1):
    for c in range(1, 5):
        ws.cell(row=r, column=c).alignment = WRAP; ws.cell(row=r, column=c).border = BOX
        ws.cell(row=r, column=c).fill = B2B_FILL
    ws.cell(row=r, column=2).font = Font(bold=True, color=INK)
    ws.row_dimensions[r].height = 46
widths(ws, {"A": 14, "B": 42, "C": 68, "D": 44})
ws.freeze_panes = "A5"

# ------------------------------------------------------------ 5. Engagement
ws = wb.create_sheet("Daily engagement")
ws["A1"] = "Daily engagement — the half of the job that isn't posting"; ws["A1"].font = TITLE_F
ws["A2"] = ("A profile with no audience grows by borrowing someone else's. This is the highest-leverage "
            "tactic on LinkedIn and almost nobody does it consistently. 15–20 minutes a day, from the "
            "founder profiles, never the company page.")
ws["A2"].alignment = WRAP
ws.append([]); ws.append(["When", "What", "Who does it", "Time"])
style_header(ws, 4, 4)
for row in [
    ("Within 15 min of publishing", "Reply to every comment, in 2–3 sentences. A new post is tested on a small slice of the network first, and comments in that window decide whether it travels further.", "Post author", "15 min"),
    ("First 60 min after publishing", "Stay reachable. Don't edit the post in this window — one source suggests editing resets the test phase, so proofread before publishing instead.", "Post author", "ongoing"),
    ("Daily, any time", "10 substantive comments on the target list. Two sentences minimum, adding a fact, a distinction or a counter-example. Never 'great post'.", "Both founders", "15–20 min"),
    ("Daily", "Log anyone from a target job title who engages. That list is the actual output of week 1.", "Lotte", "5 min"),
    ("Friday", "Refresh the target list. Drop accounts that never engage back.", "Lotte", "20 min"),
]:
    ws.append(list(row))
r0 = ws.max_row + 2
ws.cell(row=r0, column=1, value="WHO TO ENGAGE WITH — build the list to 30–50 accounts in week 1").font = SUB_F
ws.append([]); ws.append(["Group", "Who", "Why them", "Target"])
style_header(ws, ws.max_row, 4)
for row in [
    ("Demand (B2B)", "Heads of Operations, Automation and Platform; founders and COOs of 10–200 person companies; agency owners who subcontract delivery", "They commission specialist work constantly and feel the counterparty risk", "20 accounts"),
    ("Builders", "People shipping AI agents in production, MCP and agent-framework maintainers", "Nearest-term users, and the most credible commenters", "15 accounts"),
    ("Payments / fintech", "Stablecoin and cross-border payments people, treasury and finance ops", "They already believe the cost argument; they amplify it", "10 accounts"),
    ("Supply (B2C)", "Specialist freelancers, small dev shops, agencies with spare capacity", "The freelancer side — smaller effort, matching the content split", "5–10 accounts"),
]:
    ws.append(list(row))
for r in range(5, ws.max_row + 1):
    for c in range(1, 5):
        cell = ws.cell(row=r, column=c)
        if cell.value is not None or c <= 4:
            cell.alignment = WRAP
            if ws.cell(row=r, column=1).value: cell.border = BOX
widths(ws, {"A": 30, "B": 64, "C": 62, "D": 16})

# ------------------------------------------------------------ 6. Measurement
ws = wb.create_sheet("Measurement")
ws["A1"] = "What we measure from day one"; ws["A1"].font = TITLE_F
ws["A2"] = ("Followers are not the goal. Conversations with the right job titles are. "
            "Week 1 sets the baseline — nothing here is a target yet.")
ws["A2"].alignment = WRAP
ws.append([]); ws.append(["Metric", "Why it matters", "Realistic benchmark", "Week 1 actual"])
style_header(ws, 4, 4)
for row in [
    ("Engagement rate per post", "The honest read on whether the hook worked", "Median 2.17–2.42% for accounts under 10k followers. Under 0.5% is the bottom quartile.", ""),
    ("Comments from target job titles", "The metric that actually predicts pipeline. Three from the right people beats thirty from nobody.", "Low single digits per post is normal. B2B tech scrolls and rarely comments.", ""),
    ("Saves", "The strongest engagement signal LinkedIn reads", "Track the trend, not the number", ""),
    ("Profile views", "Intent. Someone read the post and went looking.", "Should rise before follower count does", ""),
    ("Follower growth", "Lagging and easy to misread", "100–300 in the first 30 days from a standing start", ""),
    ("Inbound conversations", "The real output. Waitlist signups, DMs from decision-makers, design-partner interest.", "First organic lead typically 60–90 days. Week 1 will be zero and that is fine.", ""),
]:
    ws.append(list(row))
r0 = ws.max_row + 2
ws.cell(row=r0, column=1, value="WHAT I'LL SEND EACH WEEK").font = SUB_F
ws.cell(row=r0 + 1, column=1, value=("One screen, every Monday: the three best posts and why they worked, the worst one and an "
                                     "honest diagnosis, the numbers against last week, and what changes this week. If a week is "
                                     "bad it says so in the first three lines.")).alignment = WRAP
for r in range(5, ws.max_row + 1):
    for c in range(1, 5):
        ws.cell(row=r, column=c).alignment = WRAP
        if ws.cell(row=r, column=1).value and r <= r0 - 2: ws.cell(row=r, column=c).border = BOX
widths(ws, {"A": 34, "B": 56, "C": 62, "D": 16})

# ------------------------------------------------------------ 7. Questions
ws = wb.create_sheet("Questions for Rik")
ws["A1"] = "What I need before anything publishes"; ws["A1"].font = TITLE_F
ws["A2"] = "Ordered by what blocks the most. Nothing here stops the calendar being reviewed — only published."
ws["A2"].alignment = WRAP
ws.append([]); ws.append(["#", "Question", "Why it matters", "Blocks"])
style_header(ws, 4, 4)
for i, (q, w, b) in enumerate([
    ("Is the hiring-and-escrow product called Tasks, and is it live, in private beta, or unannounced?",
     "It decides whether posts say 'you can do this' or 'we're building this'. I've written week 1 so it's true either way, but I won't guess in public.",
     "W1-04, W1-07"),
    ("Who is Founder 2, and will both founders actually post and comment?",
     "The whole plan rests on the founder profiles. If only one is willing, I'd rather rebuild the split now than miss it in week three.",
     "Everything"),
    ("Can I have 20 minutes with each founder before we start?",
     "The bracketed lines are theirs — a real number, a real opinion. That's what stops the posts reading as machine-written, which the algorithm does penalise.",
     "W1-02, W1-06, W1-08"),
    ("What can we say publicly about what ships next, and when?",
     "Build-in-public needs a roadmap I'm allowed to describe.",
     "W1-07"),
    ("Brand assets — logo, fonts, colour hexes. Is there a brand guide?",
     "I can build one if not, but I'd rather match what exists. Needed before the carousel is designed.",
     "W1-01, W1-04, W1-07"),
    ("What's the CTA? Waitlist, site, or just follow?",
     "Changes the last slide of the carousel and the close of several posts.",
     "W1-01"),
    ("Anything legally off-limits? Securities language, custody claims, specific jurisdictions?",
     "This is a payments product. I'd rather know the boundary than find it.",
     "All"),
    ("Who approves, and how fast?",
     "48 hours keeps a weekly calendar moving. Longer and I'd batch two weeks at a time instead.",
     "All"),
    ("Do I get page admin and analytics access, or do you publish?",
     "Affects whether I can report properly from week 1.",
     "Reporting"),
], start=1):
    ws.append([i, q, w, b])
for r in range(5, ws.max_row + 1):
    for c in range(1, 5):
        ws.cell(row=r, column=c).alignment = WRAP; ws.cell(row=r, column=c).border = BOX
    ws.cell(row=r, column=2).font = Font(bold=True, color=INK)
    ws.row_dimensions[r].height = 58
widths(ws, {"A": 6, "B": 62, "C": 76, "D": 20})
ws.freeze_panes = "A5"

for s in wb.worksheets:
    s.sheet_view.showGridLines = False
wb.save(OUT_XLSX)
print("xlsx:", OUT_XLSX, os.path.getsize(OUT_XLSX), "bytes")

# ------------------------------------------------------------ markdown + csv
os.makedirs(f"{ROOT}/02-linkedin/calendar", exist_ok=True)
os.makedirs(f"{ROOT}/02-linkedin/post-bank", exist_ok=True)

with open(f"{ROOT}/02-linkedin/calendar/2026-10-05-week1.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Date","Day","Time (CET)","Account","Audience","Pillar","Format","Hook",
                "Pain point","CTA","Visual","Why this post","Status"])
    for p in POSTS:
        w.writerow([p["date"],p["day"],p["time"],acct(p),p["audience"],
                    f'{p["pillar"]}. {PILLARS[p["pillar"]]}',p["fmt"],p["hook"],p["pain"],
                    p["cta"],p["visual"],p["why"],"Draft — for review"])

with open(f"{ROOT}/02-linkedin/calendar/2026-10-05-week1.md", "w") as f:
    f.write(f"# Week 1 calendar — {WEEK['start']} to {WEEK['end']}\n\n")
    f.write(f"_{WEEK['note']}_\n\n")
    f.write("9 posts. Founder profiles are the main channel; the company page supports.\n\n")
    f.write("| Date | Day | Time | Account | Audience | Pillar | Format | Hook | Status |\n")
    f.write("|---|---|---|---|---|---|---|---|---|\n")
    for p in POSTS:
        hook = p["hook"].replace("|", "\\|")
        f.write(f'| {p["date"]} | {p["day"]} | {p["time"]} | {acct(p)} | {p["audience"]} | '
                f'{p["pillar"]}. {PILLARS[p["pillar"]]} | {p["fmt"]} | {hook} | Draft |\n')

with open(f"{ROOT}/02-linkedin/post-bank/2026-10-05-week1-posts.md", "w") as f:
    f.write(f"# Week 1 posts — full copy ({WEEK['start']} to {WEEK['end']})\n\n")
    f.write("Ready to paste. `[SQUARE BRACKETS]` are deliberate gaps: either a fact to confirm "
            "with Rik, or a line only the founder can write.\n\n---\n\n")
    for p in POSTS:
        f.write(f'## {p["id"]} · {p["day"]} {p["date"]} {p["time"]}\n\n')
        f.write(f'**{acct(p)}** · {p["audience"]} · Pillar {p["pillar"]}: {PILLARS[p["pillar"]]} · {p["fmt"]}\n\n')
        f.write(f'**Why this post:** {p["why"]}\n\n')
        f.write(f'**Pain point:** {p["pain"]}\n\n')
        f.write("### Post text\n\n```\n" + p["body"] + "\n```\n\n")
        if p.get("carousel"):
            f.write("### Carousel slides\n\n| Slide | Headline | Body |\n|---|---|---|\n")
            for s, h, b in p["carousel"]:
                f.write(f"| {s} | {h} | {b} |\n")
            f.write("\n")
        f.write(f'**Visual:** {p["visual"]}\n\n**Sources:** {p["sources"]}\n\n---\n\n')
print("markdown + csv written")
