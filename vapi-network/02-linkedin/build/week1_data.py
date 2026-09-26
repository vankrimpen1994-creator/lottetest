# -*- coding: utf-8 -*-
"""Week 1 content data for vAPI Network. Single source of truth.
Emits: calendar.md, posts.md, calendar.csv and the Google Sheet workbook.

Rules honoured (see ../../CLAUDE.md and the onderzoeksbrief):
- No invented vAPI numbers. Placeholders are visible: [LIKE THIS].
- 3 fixed pillars only. No polls. Links not central to any post.
- Founder profiles are the main channel; company page supports.
"""

WEEK = {
    "label": "Week 1",
    "start": "2026-10-05",
    "end": "2026-10-09",
    "note": ("Dates assume onboarding completes the week of 28 Sep and the client "
             "goes live the first full week of October, per Rik's 'early October' start. "
             "Shift the whole grid by whole weeks if that moves."),
}

# Cadence ramps rather than opening at full speed. At zero followers a post
# reaches almost nobody, so week 1 exists to make the profiles worth landing on
# while the reach is built by the daily commenting routine. No account posts
# more than twice in week 1.
RAMP = {
    # week: (Mark, Founder 2, company page, total)
    1: (2, 2, 2, 6),
    2: (3, 2, 2, 7),
    3: (3, 3, 2, 8),
    4: (3, 3, 2, 8),   # steady state; 3/founder/week is the floor for growth
}

# Notion is authoritative for scheduling:
# https://app.notion.com/p/3e767a3a5a8a81aa92c4c2c039a48b89
# Post IDs (P-01...) are stable draft references, not week numbers.

ACCOUNTS = {
    "mark":    {"name": "Mark [FOUNDER 1]", "handle": "X: @MarkTbuilds",
                "role": "B2B lead voice — main channel", "colour": "DCE9F7"},
    "founder2":{"name": "[FOUNDER 2: NAME]", "handle": "[HANDLE]",
                "role": "B2B + the smaller B2C (freelancer) stream", "colour": "DFEFDC"},
    "company": {"name": "vAPI Network (company page)", "handle": "@vAPI_Network",
                "role": "Informational + credibility. Supports the founders.", "colour": "F2E6CC"},
}

PILLARS = {
    1: "The agent economy",
    2: "Payments & escrow",
    3: "Build in public",
}

# ---------------------------------------------------------------- posts
POSTS = [
    dict(
        id="P-07", date="2026-10-12", day="Monday", time="08:30 CET", week=2,
        account="mark", audience="B2B", pillar=2, fmt="Carousel (10 slides) + text",
        hook="Paying a contractor in another country costs more than you think. Not the rate — the moving of the money.",
        pain="Cross-border contractor payments quietly eat 3–5% and a working week.",
        cta="Question: what does your finance team budget for cross-border contractor payments?",
        why=("Opens the week on the strongest B2B angle: money, not technology. Carousels are the top "
             "format in every 2026 dataset (Socialinsider 7.00% vs 5.20% average). Cost framing follows "
             "the rule for sceptical business audiences — speed, cost, reliability, never ideology."),
        body="""Paying a contractor in another country costs more than you think.

Not the rate. The moving of the money.

Request Finance put numbers on it this year: $25–50 to send an international transfer, another $10–30 for the recipient to receive it, a 1.5–3% FX spread if either side isn't working in dollars, and 2–5 business days before anyone sees anything.

On a $2,000 project that's up to 5% gone, and a week, before the work has even been reviewed.

We've been building on the other version of this. Payment in digital dollars (USDC), settled in under a minute, for roughly one to ten cents, with no FX spread.

But speed on its own doesn't fix the real problem, which is older than any of this: do you pay before the work, or after? One of you carries the risk either way.

That's what the escrow step is for. The money is locked, not sent, and it releases when the work is accepted.

The carousel breaks down where the money actually goes today.

What does your finance team currently budget for cross-border contractor payments?""",
        carousel=[
            ("1 — Cover", "What it actually costs to pay a contractor abroad", "The fees nobody puts in the project budget. 2026 figures."),
            ("2", "The rate is not the cost", "You agreed $2,000. That is not what leaves your account, and it is not what arrives."),
            ("3", "Sending: $25–50", "Standard international transfer fee. Charged to you. Per payment."),
            ("4", "Receiving: $10–30", "Charged to them. They experience it as a pay cut they didn't agree to."),
            ("5", "FX spread: 1.5–3%", "If either side isn't working in dollars. On $2,000, up to $60."),
            ("6", "Time: 2–5 business days", "Longer if it meets a weekend or a public holiday."),
            ("7", "Total: up to ~5%, and a week", "Before anyone has reviewed whether the work is any good."),
            ("8", "The alternative: digital dollars", "A USDC transfer settles in under a minute, costs roughly $0.01–0.10, and has no FX spread."),
            ("9", "Speed isn't the whole problem", "Fast payment still doesn't answer: do I pay before the work, or after? Escrow does. The money is locked, not sent, until the work is accepted."),
            ("10 — CTA", "We're building that at vAPI Network", "[CTA — CONFIRM WITH RIK: follow, waitlist, or site]"),
        ],
        visual=("10-slide PDF carousel, 1080x1350. One figure per slide, very large type. "
                "Source line 'Source: Request Finance, 2026' small at the bottom of slides 3-6 and 8. "
                "Watermark 'vAPI Network' bottom-left on every slide."),
        sources="Request Finance, stablecoin B2B guide, 2026 (via onderzoeksbrief §8).",
    ),
    dict(
        id="P-05", date="2026-10-08", day="Thursday", time="17:00 CET", week=1,
        account="founder2", audience="B2C", pillar=2, fmt="Text (+ optional simple graphic)",
        hook="You finished the work three weeks ago. The invoice is 'being processed.'",
        pain="Freelancers fund their clients' cash flow, interest-free, with no way to opt out.",
        cta="Question: what's the longest you've waited to be paid for work you'd already delivered?",
        why=("Launches the B2C (supply-side) stream on the same subject as the B2B posts — getting paid "
             "for scoped work — so topic authority isn't diluted. Opens on a lived moment rather than a "
             "product, which is what the algorithm rewards over recycled advice."),
        body="""You finished the work three weeks ago. The invoice is "being processed."

Every freelancer knows this specific kind of tired. Not the work — the waiting. The polite follow-up you rewrite four times so it doesn't read as desperate. The 30-day terms that quietly became 60.

And the part nobody says out loud: you funded that client's cash flow, interest-free, because there was no way not to.

The sequence today:
→ You scope it, loosely, in a thread
→ You do the work
→ You invoice
→ You wait
→ You chase

The sequence we're building:
→ Both sides sign the scope and the price
→ The client locks the money in escrow before you start
→ You do the work knowing it is already funded
→ It's accepted, payment releases
→ No invoice. No chase.

You still have to do good work. Nothing here protects anyone from that. You just stop carrying the risk of someone else's payment cycle on top of it.

[FOUNDER 2: one specific line here about why this matters to you personally — a time you waited, or watched someone wait. The post works without it and lands twice as hard with it.]

If you freelance: what's the longest you've ever waited to get paid for work you'd already delivered?""",
        visual=("Optional: simple two-column 'today vs. what we're building' graphic, 1080x1350. "
                "Text-only is fine and may perform better. Watermark 'vAPI Network'."),
        sources="None required — no external figures used.",
    ),
    dict(
        id="P-03", date="2026-10-07", day="Wednesday", time="08:30 CET", week=1,
        account="founder2", audience="B2B", pillar=1, fmt="Text",
        hook="AI agents can write your code, research your market and draft your contracts. They still can't get paid.",
        pain="Teams running agents have no safe way to let them transact — card-and-hope, or an approval queue that defeats the point.",
        cta="Question: if you're running agents in production, how are you handling spend today?",
        why=("Hook #1 from the research brief, which names a specific audience and a concrete gap. "
             "Establishes the category before selling anything — pillar 1 is the widest net and this is "
             "the post most likely to be shared by people who aren't customers yet."),
        body="""AI agents can write your code, research your market and draft your contracts.

They still can't get paid.

It's a strange gap once you notice it. We've given software the ability to do the work and not the ability to transact for it. Every agent that needs to buy data, commission a specialist or pay for compute hits the same wall: a checkout form built for a human with a billing address and a patience threshold.

So teams do one of three things.

→ Put a corporate card behind the agent and hope
→ Build an approval queue, which removes most of the reason you automated it
→ Keep the agent read-only and do the buying by hand

None of those scale. The first is the one that worries finance, and they're right to be worried.

What's actually missing is narrower than "payments". It's three things:

1. A way for software to pay per task, in small amounts, without holding an account
2. A hard spend limit enforced before the payment is signed, not reported after it's gone
3. A record of every payment that the business owns, not one it logs into

That's the layer we're building at vAPI Network. Payment in digital dollars, per task, with the limits set before anything moves.

If you're running agents in production: how are you handling spend today?""",
        visual="None, or a plain quote card of the first two lines. Text-only is the default for this one.",
        sources="None required.",
    ),
    dict(
        id="P-02", date="2026-10-06", day="Tuesday", time="12:00 CET", week=1,
        account="company", audience="B2B", pillar=1, fmt="Text + single image",
        hook="vAPI Network is where businesses hire AI agents and specialists for scoped work — and where the payment is held until the work is accepted.",
        pain="Prospects who land on the page don't know what the company is in one sentence.",
        cta="Soft: follow for build updates.",
        why=("The company page's job this week is comprehension and credibility, not reach. This is the "
             "post a prospect reads after clicking a founder's profile. Every credibility marker in one "
             "place: open source, non-custodial, audited, built on a standard with recognisable backers."),
        body="""vAPI Network is where businesses hire AI agents and specialists for scoped work, and where the payment is held until the work is accepted.

How it fits together:

Scope — both sides agree what "done" means and what it costs, before anything starts.
Escrow — the buyer locks the payment in digital dollars (USDC). Held, not sent.
Review — the work is delivered and checked against the scope that was signed.
Release — accepted work releases payment automatically.

What separates this from a directory: a directory introduces you to someone. A marketplace holds the money while you find out whether the introduction was any good.

A few things worth knowing about how it's built:

· Open source under Apache 2.0. The code is public.
· Non-custodial. Keys are generated and encrypted on your own machine. We never hold your funds and cannot move them.
· No telemetry leaves your machine by default.
· Built on x402, an open payment standard now governed by the Linux Foundation, with Google, Visa, Mastercard, Stripe, AWS and Circle among its members.
· Security audit completed by Hacken.

Call — paying for individual services per request — is live today. [CONFIRM WITH RIK: exactly what we can say publicly about the hiring/escrow product and its name.]

Follow along for build updates as the rest ships.""",
        visual=("Single image, 1200x1500: the four-step flow Scope → Escrow → Review → Release as a "
                "clean horizontal or vertical diagram. Muted, technical, no gradients. Watermark."),
        sources=("x402 / Linux Foundation governance and members: Linux Foundation announcement, April 2026. "
                 "Hacken audit and Apache 2.0: vAPI Network GitHub repo. CONFIRM both with Rik before publishing."),
    ),
    dict(
        id="P-01", date="2026-10-05", day="Monday", time="08:30 CET", week=1,
        account="mark", audience="B2B", pillar=1, fmt="Text",
        hook="Most 'AI agent marketplaces' are directories. A marketplace needs one thing directories don't: a way to hold the money until the work is done.",
        pain="Buyers can't tell competing 'agent marketplaces' apart, so they trust none of them.",
        cta="Question: what would you need to see before letting an agent commission work on your company's behalf?",
        why=("Hook #5 from the brief — a defensible opinion, which the algorithm rewards over recycled "
             "advice and which invites the substantive comments that weigh more than likes. Draws a "
             "category line that happens to favour vAPI without naming a competitor."),
        body="""Most "AI agent marketplaces" are directories.

A directory tells you who exists. You still have to email them, agree a price across three messages, send a deposit, and hope.

A marketplace does the one thing a directory can't: it holds the money until the work is done.

That's not a feature. It's the reason marketplaces work at all. Upwork isn't valuable because it lists freelancers — you could list freelancers in a spreadsheet. It's valuable because neither side has to trust the other first.

Now apply that to agents.

If an AI agent is going to commission work — from another agent, or from a person — it needs the same primitive. Scope agreed up front, because software can't negotiate ambiguity. Money locked rather than sent. Released when the work is accepted. And something to fall back on when it goes wrong, because sometimes it will.

Without that, an "agent marketplace" is a list with better branding. With it, software can commission a piece of work at 2am for $4 and nobody has to be awake.

We're building the second thing. It's harder, it demos badly, and it's the part that matters.

What would you need to see before you'd let an agent commission work on your company's behalf?""",
        visual="None. Text-only. Optionally a plain quote card of lines 1-3 for reuse later.",
        sources="None required.",
    ),
    dict(
        id="P-09", date="2026-10-15", day="Thursday", time="08:30 CET", week=2,
        account="founder2", audience="B2C", pillar=1, fmt="Text",
        hook="An AI agent might be your next client.",
        pain="Freelancers are anxious that agents replace them; the reframe is that agents commission them.",
        cta="Question: would you take a job commissioned by software, if the money was already in escrow?",
        why=("Second and final B2C post of the week. Turns the freelancer's fear of AI into a demand "
             "source, which is the only honest way to recruit supply here. Stays inside pillar 1, so "
             "Founder 2's profile still reads as one subject to the algorithm."),
        body="""An AI agent might be your next client.

That reads like a headline. It's closer to a scheduling problem.

Here's the shape of it. A company runs an agent that handles a workflow end to end. Partway through it hits something it can't do well — a translation that needs a native speaker, a design judgement, a dataset someone has to actually verify. Today the workflow stops and waits for a human to notice it stopped.

The alternative is that it commissions the work. Posts a scoped task, funds it, and a person picks it up.

For freelancers that's a new demand source, and it has a few properties human clients often don't:

→ The scope is written down, because software can't be vague
→ The money is locked before you start
→ It has no opinion about your rate at 11pm on a Sunday

The first question everyone asks is what happens when it goes wrong. Fair question. The work is reviewed against the signed scope before payment releases, and a disagreement goes to a defined dispute route rather than an argument you have to win.

[FOUNDER 2: your honest view — is this exciting or unsettling? Say which. A straight opinion will outperform a balanced one here.]

Freelancers: would you take a job commissioned by software, if the money was already sitting in escrow?""",
        visual="None. Text-only.",
        sources="None required.",
    ),
    dict(
        id="P-06", date="2026-10-09", day="Friday", time="12:00 CET", week=1,
        account="company", audience="B2B", pillar=3, fmt="Text + single image",
        hook="Call is live.",
        pain="Pre-launch companies look like vapourware unless something concrete has shipped.",
        cta="Soft: read the code.",
        why=("The company page's second job is proof that something real exists. Names the three "
             "constraints as mechanisms rather than adjectives, which is what converts a technical "
             "reader. Honest about what hasn't shipped, which is a trust asset pre-launch."),
        body="""Call is live.

It's the first of the pieces we're shipping, and the smallest one worth explaining properly.

Call lets an agent find a service, see what it costs, and pay for it per request. No account, no dashboard, no subscription. Payment settles in digital dollars (USDC) on Base.

Three constraints we held ourselves to:

1. Your key never leaves your machine. It's generated locally and encrypted under a passphrase. We don't hold funds and we can't move them.

2. Spend limits are checked before a payment is signed, not reported afterwards. You set caps per call, per wallet and per day. A limit that's enforced after the money has gone is a receipt, not a control.

3. Every payment writes to a local append-only ledger. The record is yours, not a dashboard you log into.

It's open source under Apache 2.0, it runs as a CLI or an MCP server, and it's been audited by Hacken.

[CONFIRM WITH RIK: what we can say publicly about what ships next, and when.]

The code is public, if you'd rather read it than take our word for it.""",
        visual=("Single image, 1200x1500: terminal-style card showing a payment receipt line. "
                "Mono type. Muted. Watermark 'vAPI Network'."),
        sources="Product facts: vAPI Network GitHub repo and onderzoeksbrief §2. CONFIRM with Rik.",
    ),
    dict(
        id="P-04", date="2026-10-08", day="Thursday", time="08:30 CET", week=1,
        account="mark", audience="B2B", pillar=3, fmt="Text",
        hook="If an AI agent does the job wrong, who gives the money back?",
        pain="Nobody trusts a marketplace whose operator also judges its disputes.",
        cta="Question to builders: what did we get wrong?",
        why=("Hook #3 from the brief. Build-in-public at its most useful: a real design decision, "
             "including the part that was contested. Asking practitioners what we got wrong is the "
             "single most reliable way to get substantive comments, which outweigh likes."),
        body="""If an AI agent does the job wrong, who gives the money back?

We spent [MARK: how long did this actually take? A real number is better than a round one] on that one question. It was the least glamorous part of building this and probably the most important.

The easy answer is "the platform decides." We didn't want that. A platform that takes a fee and also settles its own disputes has a conflict everyone using it can see, even when it behaves well.

Where we landed:

→ Scope and price are signed by both sides before work starts. Most disputes die here, because "done" got defined while nobody was annoyed.

→ The money sits in escrow. Not with us. Locked, and neither side can quietly walk off with it.

→ Accepted work releases payment automatically. No approval step for someone to forget about.

→ A dispute goes to three independent reviewers. Two matching votes decide: release, refund, or split.

The split option was the argument internally. It's messy, it's harder to explain, and it's also what actually happens in real disputes — the work was 70% there and both people are partly right. Pretending otherwise just moves the unfairness somewhere else.

[MARK: the specific thing that changed your mind during this. One sentence. It's the best part of the post and only you can write it.]

Anyone who's built dispute resolution before: what did we get wrong?""",
        visual="None. Text-only.",
        sources="None required.",
    ),
    dict(
        id="P-08", date="2026-10-14", day="Wednesday", time="12:00 CET", week=2,
        account="founder2", audience="B2B", pillar=2, fmt="Text",
        hook="Three questions to ask before you let software spend your company's money.",
        pain="Buyers can't evaluate agent-payment tools because the differences aren't visible from a landing page.",
        cta="Question: which of the three would your finance team ask first?",
        why=("Closes the week with a saveable checklist — saves are the strongest engagement signal on "
             "LinkedIn. Deliberately vendor-neutral so it travels beyond the follower base, with vAPI's "
             "answers stated plainly rather than sold."),
        body="""Three questions to ask before you let software spend your company's money.

Not rhetorical. We get asked a version of these every week, and the answers are more or less the whole product.

1. When is the limit checked?

Before the payment is signed, or after it's already gone? Most tools report spend. Fewer prevent it. If the cap is applied after the fact, it isn't a control, it's a receipt.

2. Who holds the funds?

If the answer is "the platform", custody has been outsourced without anyone using that word. Worth asking what happens to your balance if that company has a bad quarter.

3. Where does the record live?

A dashboard you log into is their record, available for as long as they feel like hosting it. A receipt written to a ledger you hold is yours. Ask which one you're getting, because at some point your auditor will.

For the record, our answers: before signing; nobody, the key stays encrypted on your own machine; a local append-only ledger you own.

But ask them of anyone, us included. This is a category where the architecture matters more than the pitch, and almost none of it is visible from a landing page.

Which of those three would your finance team ask first?""",
        visual="Optional: plain 3-point checklist card, 1200x1500, for saves. Text-only also works.",
        sources="None required.",
    ),
]
