---
description: Produce the weekly snapshot or monthly dashboard
---
Produce a performance report for vAPI Network. Type/period: $ARGUMENTS
(default: weekly snapshot for the week just ended)

Read `vapi-network/01-strategy/kpi-framework.md` and prior reports in
`vapi-network/05-ops/reporting/`.

**Weekly snapshot** — must fit one screen:
- Tier 1 metrics vs. last week, with direction
- Top 3 posts and *why* they worked (hook, format, pillar, timing)
- Worst post and the honest diagnosis
- Comments from ICP-matching titles — count and notable names
- What we change this week, specifically

**Monthly dashboard:** all of the above plus Tier 2 and Tier 3, pillar-by-pillar
performance, progress against the target bands in `kpi-framework.md`, what we learned,
next month's plan, and one explicit ask of the client.

Save to `vapi-network/05-ops/reporting/YYYY-MM-DD-<weekly|monthly>.md`.

**Use only real numbers.** Any figure not supplied or not in a file gets
`[NEEDS DATA: ...]`. Never estimate performance. If we're below the target band, say so
in the first three lines — bad news early is the whole value of reporting.
