#!/usr/bin/env python3
"""Stop / SessionEnd hook — archives the session transcript into the project.

Writes two things per session:
  logs/transcripts/<date>-<sid>.jsonl   raw, complete
  logs/transcripts/<date>-<sid>.md      readable digest of prompts + responses

Fails silently (exit 0) so it can never block a session.
"""
import json, os, shutil, sys, datetime, pathlib

def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return

    tp = data.get("transcript_path")
    if not tp or not os.path.exists(tp):
        return

    root = pathlib.Path(
        os.environ.get("CLAUDE_PROJECT_DIR")
        or pathlib.Path(__file__).resolve().parents[2]
    )
    # Which client folder to log into: first line of .claude/active-client, else vapi-network.
    client = "vapi-network"
    try:
        c = (root / ".claude" / "active-client").read_text().splitlines()[0].strip()
        if c and (root / c).is_dir():
            client = c
    except Exception:
        pass
    outdir = root / client / "logs" / "transcripts"
    outdir.mkdir(parents=True, exist_ok=True)

    sid = (data.get("session_id") or "unknown")[:12]
    day = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    stem = f"{day}-{sid}"

    try:
        shutil.copyfile(tp, outdir / f"{stem}.jsonl")
    except Exception:
        pass

    lines = [f"# Session transcript — {day} · `{sid}`\n",
             "_Auto-exported. Raw JSONL alongside this file._\n"]
    try:
        with open(tp, encoding="utf-8") as fh:
            for raw in fh:
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    ev = json.loads(raw)
                except Exception:
                    continue
                role = ev.get("type")
                msg = ev.get("message") or {}
                content = msg.get("content")
                if isinstance(content, str):
                    parts = [content]
                elif isinstance(content, list):
                    parts = [c.get("text", "") for c in content
                             if isinstance(c, dict) and c.get("type") == "text"]
                else:
                    parts = []
                text = "\n".join(p for p in parts if p).strip()
                if not text:
                    continue
                if role == "user":
                    lines.append(f"\n---\n\n## ▶ Prompt\n\n{text}\n")
                elif role == "assistant":
                    lines.append(f"\n### ◀ Response\n\n{text}\n")
    except Exception:
        pass

    try:
        (outdir / f"{stem}.md").write_text("\n".join(lines), encoding="utf-8")
    except Exception:
        pass

if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
