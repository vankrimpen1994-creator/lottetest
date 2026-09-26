# -*- coding: utf-8 -*-
"""Flatten week 1 into a single-tab TSV that reads well in an unformatted Google Sheet.
Post bodies are split one paragraph per row, so nothing depends on cell wrapping."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from week1_data import WEEK, ACCOUNTS, PILLARS, POSTS

R = []
def row(*cells):
    R.append([str(c).replace("\t", " ").replace("\r", "").strip() for c in cells])
def blank(n=1):
    for _ in range(n): R.append([""])

acct = lambda p: ACCOUNTS[p["account"]]["name"]

row("vAPI NETWORK — LINKEDIN CONTENT CALENDAR")
row(f"{WEEK['label']}: Monday {WEEK['start']} to Friday {WEEK['end']}  ·  9 posts")
row("Prepared by Lotte for Coconnect (Rik) — first draft, for review")
blank()
row("THE GOAL")
row("Give the brand a voice it doesn't have yet, and point it at one job: getting businesses to bring their hiring to vAPI Network.")
row("Coconnect covers the freelancer (supply) side. LinkedIn's job here is the demand side, with a small deliberate freelancer stream so the two sides can see each other.")
blank()
row("HOW THE THREE ACCOUNTS ARE USED")
row("Account", "Posts this week", "Job")
for k, n in (("mark", 3), ("founder2", 4), ("company", 2)):
    row(ACCOUNTS[k]["name"], n, ACCOUNTS[k]["role"])
row("Why the founders carry it: across a 2026 study of company pages vs. personal profiles, personal profiles averaged 2.6% engagement against 1.6%, and 237% more comments per post.")
blank()
row("THE THREE CONTENT PILLARS — every post is exactly one of these")
row("1. " + PILLARS[1], "What changes when software buys and commissions work. Who is liable, how trust works.")
row("2. " + PILLARS[2], "Why agents need a payment layer, why escrow, why digital dollars as the rail.")
row("3. " + PILLARS[3], "Pre-launch updates, decisions, mistakes and lessons from the founders.")
row("Only three, on purpose: LinkedIn's ranking model weighs whether an account has earned the right to talk about a topic. An account that posts too widely can't be classified, so it isn't shown.")
blank()
row("THE B2B / B2C QUESTION — the one judgement call worth flagging")
row("Rik asked whether to split B2B and B2C across separate profiles. Splitting is cleaner for topic authority, and that was my instinct on the call.")
row("What I've done instead: Founder 2 carries both, but the B2C posts stay inside the same three pillars — the freelancer's side of getting paid for scoped work.")
row("The subject never changes, only who is being addressed. Topic authority survives, and we don't need a fourth account nobody has time to run.")
row("If the freelancer side ever needs real volume, that's the moment to split it onto its own profile. It doesn't need it at two posts a week.")
blank()
row("ANYTHING IN [SQUARE BRACKETS] IS A DELIBERATE GAP")
row("[CONFIRM WITH RIK: ...]", "A fact I won't publish on a guess. There are five.")
row("[MARK: ...] / [FOUNDER 2: ...]", "A line only the founder can write — a real number, a real opinion. LinkedIn reportedly penalises text that reads as purely machine-written, so these are load-bearing.")
blank()
row("NOTE ON DATES", WEEK["note"])
blank(2)

row("———  THE CALENDAR  ———")
blank()
row("Date", "Day", "Time CET", "Account", "Audience", "Pillar", "Format", "Status", "Hook — the first line that has to earn the click")
for p in POSTS:
    row("'" + p["date"], p["day"], p["time"].replace(" CET", ""), acct(p), p["audience"],
        f'{p["pillar"]}. {PILLARS[p["pillar"]]}', p["fmt"], "Draft", p["hook"])
blank(2)

row("———  POST COPY — READY TO PASTE  ———")
row("Each post is broken into one row per paragraph so it reads without needing cell wrapping.")
blank()
for p in POSTS:
    row(f'{p["id"]} — {p["day"]} {p["date"]} at {p["time"]}')
    row("", f'{acct(p)}  ·  {p["audience"]}  ·  Pillar {p["pillar"]}: {PILLARS[p["pillar"]]}  ·  {p["fmt"]}')
    row("", f'WHY THIS POST: {p["why"]}')
    row("", f'PAIN POINT: {p["pain"]}')
    blank()
    row("", "POST TEXT:")
    for line in p["body"].split("\n"):
        row("", "", line)
    blank()
    row("", f'VISUAL: {p["visual"]}')
    row("", f'SOURCES: {p["sources"]}')
    blank(2)

car = [p for p in POSTS if p.get("carousel")][0]
row("———  MONDAY'S CAROUSEL — SLIDE BY SLIDE  ———")
row("10 slides, 1080x1350, exported as a PDF. One idea per slide, very large type, legible at thumbnail size. 'vAPI Network' watermark bottom-left on every slide.")
blank()
row("Slide", "Headline", "Body copy")
for s, h, b in car["carousel"]:
    row(s, h, b)
row("Design notes", "Source line 'Source: Request Finance, 2026' at the bottom of slides 3-6 and 8. Slide 7 is the screenshot slide — make the 5% dominant. Slide 8 switches to the accent colour: the deck turns positive. Confirm the slide 10 CTA with Rik before export.")
blank(2)

row("———  DAILY ENGAGEMENT — THE HALF OF THE JOB THAT ISN'T POSTING  ———")
row("A profile with no audience grows by borrowing someone else's. 15-20 minutes a day, from the founder profiles, never the company page.")
blank()
row("When", "What", "Who", "Time")
for r_ in [
    ("Within 15 min of publishing", "Reply to every comment in 2-3 sentences. A new post is tested on a small slice of the network first, and comments in that window decide whether it travels.", "Post author", "15 min"),
    ("First 60 min after publishing", "Stay reachable. Don't edit the post in this window — one source suggests editing resets the test phase, so proofread before publishing.", "Post author", "ongoing"),
    ("Daily", "10 substantive comments on the target list. Two sentences minimum, adding a fact, a distinction or a counter-example. Never 'great post'.", "Both founders", "15-20 min"),
    ("Daily", "Log anyone from a target job title who engages. That list is the real output of week 1.", "Lotte", "5 min"),
    ("Friday", "Refresh the target list. Drop accounts that never engage back.", "Lotte", "20 min"),
]: row(*r_)
blank()
row("WHO TO ENGAGE WITH — build to 30-50 accounts in week 1")
row("Group", "Who", "Why them", "Target")
for r_ in [
    ("Demand (B2B)", "Heads of Operations, Automation and Platform; founders and COOs of 10-200 person companies; agency owners who subcontract delivery", "They commission specialist work constantly and feel the counterparty risk", "20 accounts"),
    ("Builders", "People shipping AI agents in production, MCP and agent-framework maintainers", "Nearest-term users, and the most credible commenters", "15 accounts"),
    ("Payments / fintech", "Stablecoin and cross-border payments people, treasury and finance ops", "They already believe the cost argument and amplify it", "10 accounts"),
    ("Supply (B2C)", "Specialist freelancers, small dev shops, agencies with spare capacity", "The freelancer side — smaller effort, matching the content split", "5-10 accounts"),
]: row(*r_)
blank(2)

row("———  MEASUREMENT  ———")
row("Followers are not the goal. Conversations with the right job titles are. Week 1 sets the baseline — nothing here is a target yet.")
blank()
row("Metric", "Why it matters", "Realistic benchmark", "Week 1 actual")
for r_ in [
    ("Engagement rate per post", "The honest read on whether the hook worked", "Median 2.17-2.42% for accounts under 10k followers. Under 0.5% is the bottom quartile.", ""),
    ("Comments from target job titles", "The metric that predicts pipeline. Three from the right people beats thirty from nobody.", "Low single digits per post is normal. B2B tech scrolls and rarely comments.", ""),
    ("Saves", "The strongest engagement signal LinkedIn reads", "Track the trend, not the number", ""),
    ("Profile views", "Intent — someone read the post and went looking", "Should rise before follower count does", ""),
    ("Follower growth", "Lagging and easy to misread", "100-300 in the first 30 days from a standing start", ""),
    ("Inbound conversations", "The real output: waitlist signups, DMs from decision-makers, design-partner interest", "First organic lead typically 60-90 days. Week 1 will be zero, and that is fine.", ""),
]: row(*r_)
blank()
row("WHAT I'LL SEND EACH WEEK")
row("One screen, every Monday: the three best posts and why they worked, the worst one and an honest diagnosis, the numbers against last week, and what changes this week. If a week is bad it says so in the first three lines.")
blank(2)

row("———  QUESTIONS FOR RIK — BEFORE ANYTHING PUBLISHES  ———")
row("Ordered by what blocks the most. None of this stops the calendar being reviewed, only published.")
blank()
row("#", "Question", "Why it matters", "Blocks")
for i, (q, w, b) in enumerate([
    ("Is the hiring-and-escrow product called Tasks, and is it live, in private beta, or unannounced?", "It decides whether posts say 'you can do this' or 'we're building this'. Week 1 is written so it's true either way, but I won't guess in public.", "W1-04, W1-07"),
    ("Who is Founder 2, and will both founders actually post and comment?", "The whole plan rests on the founder profiles. If only one is willing, I'd rather rebuild the split now than miss it in week three.", "Everything"),
    ("Can I have 20 minutes with each founder before we start?", "The bracketed lines are theirs — a real number, a real opinion. That's what stops the posts reading as machine-written.", "W1-02, W1-06, W1-08"),
    ("What can we say publicly about what ships next, and when?", "Build-in-public needs a roadmap I'm allowed to describe.", "W1-07"),
    ("Brand assets — logo, fonts, colour hexes. Is there a brand guide?", "I can build one if not, but I'd rather match what exists. Needed before the carousel is designed.", "W1-01, W1-04, W1-07"),
    ("What's the CTA — waitlist, site, or just follow?", "Changes the last slide of the carousel and the close of several posts.", "W1-01"),
    ("Anything legally off-limits? Securities language, custody claims, specific jurisdictions?", "This is a payments product. I'd rather know the boundary than find it.", "All"),
    ("Who approves, and how fast?", "48 hours keeps a weekly calendar moving. Longer and I'd batch two weeks at a time instead.", "All"),
    ("Do I get page admin and analytics access, or do you publish?", "Affects whether I can report properly from week 1.", "Reporting"),
], start=1):
    row(i, q, w, b)

# Drive parses uploads as CSV, so emit real CSV with proper quoting.
import csv, io, re
# Guard any cell Sheets would read as a formula.
for r in R:
    for i, c in enumerate(r):
        if c[:1] in ("=", "+", "@"):
            r[i] = "'" + c
buf = io.StringIO()
w = csv.writer(buf, lineterminator="\n")
for r in R:
    w.writerow(r)
out = buf.getvalue()
width = max(len(r) for r in R)
path = "/tmp/claude-0/-home-user-lottetest/62c57f79-7652-5687-97b1-47eab89dda0b/scratchpad/week1.csv"
open(path, "w").write(out)
# round-trip check
back = list(csv.reader(io.StringIO(out)))
assert len(back) == len(R), (len(back), len(R))
for a, b in zip(back, R):
    assert a == b, (a, b)
bad = [c for r in back for c in r if c[:1] == "="]
print(f"rows={len(R)} cols={width} bytes={len(out)} round-trip=OK formula-risk-cells={len(bad)}")
