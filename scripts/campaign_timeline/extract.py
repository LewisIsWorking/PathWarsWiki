"""Split a campaign's months into scenes with a free model, and save them.

    python scripts/campaign_timeline/extract.py \
        --source ../telegram-pbp-reminder/data/pbp_logs/Magni_Guard \
        --code C04 --name "Magni Guard" --data timelines/C04-Magni-Guard.json

Runs on Lewis's machine, not in CI: it needs the local ``delegate`` skill.

Only months that are new, or whose message count has changed, are sent.
Everything Lewis writes into the data file by hand (``in_game``,
``renames``, ``area_renames``) is left alone. A month the model gets wrong twice is left
out and reported, never saved half right.
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from messages import read_campaign  # noqa: E402
from scenes import build_prompt, parse_reply, validate  # noqa: E402

DELEGATE = Path.home() / ".claude" / "skills" / "delegate" / "delegate.ps1"
USAGE = DELEGATE.parent / "usage.jsonl"
WRAPPER = Path(__file__).parent / "delegate-utf8.ps1"
ATTEMPTS = 2


def load(path: Path, code: str, name: str) -> dict:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"code": code, "campaign": name, "months": {},
            "in_game": {}, "renames": {}, "area_renames": {}}


def save(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")


def place(scene: dict) -> str:
    """ "Area > Room", as the prompt lists places."""
    return f"{scene['area']} > {scene['location']}"


def known_locations(data: dict) -> list[str]:
    seen: list[str] = []
    for month in sorted(data["months"]):
        for s in data["months"][month]["scenes"]:
            if place(s) not in seen:
                seen.append(place(s))
    return seen


def ended_at(data: dict, month: str) -> str | None:
    """Where the party was at the end of the last saved month before this one."""
    earlier = [m for m in sorted(data["months"]) if m < month]
    return place(data["months"][earlier[-1]]["scenes"][-1]) if earlier else None


def ask(prompt: str) -> tuple[str, str]:
    """Send one prompt through the delegate skill. Returns (reply, model)."""
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False,
                                     encoding="utf-8") as f:
        f.write(prompt)
        prompt_file = f.name
    try:
        proc = subprocess.Popen(
            ["pwsh", "-NoProfile", "-File", str(WRAPPER),
             "-Task", "Follow the instructions in the attached file exactly. "
                      "Reply with only the JSON object it asks for.",
             "-File", prompt_file],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, encoding="utf-8", errors="replace")
        reply, _ = proc.communicate(timeout=900)
    finally:
        os.unlink(prompt_file)
    return reply, _model_for(proc.pid)


def _model_for(pid: int) -> str:
    """The model the delegate call ended up on, from its own usage log.

    ⚠️ Matched on pid. Other sessions on this machine share the log, so its
    last line is not necessarily this call's.
    """
    try:
        for line in reversed(USAGE.read_text(encoding="utf-8").splitlines()):
            row = json.loads(line)
            if row.get("pid") == pid:
                return row.get("model", "unknown")
    except (OSError, ValueError):
        pass
    return "unknown"


def extract(source: Path, data_path: Path, code: str, name: str,
            group: str) -> int:
    data = load(data_path, code, name)
    months = read_campaign(source, group)
    failed = []
    for month, messages in months.items():
        done = data["months"].get(month)
        if not messages or (done and done["messages"] == len(messages)):
            continue
        prompt = build_prompt(messages, known_locations(data),
                              ended_at(data, month))
        for attempt in range(1, ATTEMPTS + 1):
            reply, model = ask(prompt)
            try:
                scenes, dropped = validate(parse_reply(reply), messages)
            except ValueError as e:
                print(f"{month}: attempt {attempt} rejected ({model}): {e}")
                continue
            data["months"][month] = {"messages": len(messages),
                                     "model": model, "scenes": scenes}
            save(data_path, data)
            note = f", dropped {len(dropped)} unquoted time cue(s)" if dropped else ""
            print(f"{month}: {len(messages)} messages -> {len(scenes)} scenes "
                  f"({model}{note})")
            break
        else:
            failed.append(month)
    if failed:
        print(f"NOT EXTRACTED (rejected {ATTEMPTS}x): {', '.join(failed)}")
    return 1 if failed else 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--data", type=Path, required=True)
    p.add_argument("--code", required=True)
    p.add_argument("--name", required=True)
    p.add_argument("--group", default="Path_Wars")
    a = p.parse_args()
    return extract(a.source, a.data, a.code, a.name, a.group)


if __name__ == "__main__":
    sys.exit(main())
