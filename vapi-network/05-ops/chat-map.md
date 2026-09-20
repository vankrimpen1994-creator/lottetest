# Chat Map — one session per job

The point of this folder: **don't run everything in one endless chat.** Each recurring
job gets its own session, started with its own slash command, so context stays clean
and output stays consistent.

Each command lives in `.claude/commands/` at the repo root and is invoked by typing
`/name` at the start of a fresh session.

| Command | Job | When | Writes to |
|---|---|---|---|
| `/weekly-content` | Plan + draft next week's 7 posts | Thursday | `02-linkedin/calendar/` + `post-bank/` |
| `/post-draft` | Draft one post on a specific angle | Ad hoc | `02-linkedin/post-bank/` |
| `/engage` | Build this week's commenting target list + draft comments | Monday | `02-linkedin/engagement-log.md` |
| `/podcast-prep` | Guest research, question set, pre-call brief | Before each recording | `03-podcast/episodes/` |
| `/podcast-repurpose` | Turn a transcript into 8–12 LinkedIn assets | After each episode | `03-podcast/episodes/` + `post-bank/` |
| `/design-brief` | Turn an approved post into a designer-ready asset brief | With each visual | `04-design/briefs/` |
| `/report` | Weekly snapshot or monthly dashboard | Monday / month-end | `05-ops/reporting/` |
| `/research` | Category, competitor or guest research with sources | Ad hoc | `01-strategy/` |

## Rules for every session
1. **One command, one job.** Don't drift — start a new session instead.
2. Claude reads `CLAUDE.md` automatically. It carries the voice rules and the
   no-invented-metrics rule, so output is consistent across sessions.
3. Everything lands in a file, not just in the chat. Chats get lost; files don't.
4. Every session is logged to `logs/` automatically — see `logs/README.md`.

## Weekly rhythm at a glance
```
MON  /engage    → target list + drafted comments        (30 min)
     /report    → last week's snapshot                  (20 min)
TUE  publish + live engagement
WED  publish · /podcast-prep if recording this week
THU  /weekly-content → next week's 7 posts drafted      (60 min)
     → send for approval (48h clock starts)
FRI  /design-brief for each approved visual             (30 min)
     /podcast-repurpose if an episode was recorded
```
