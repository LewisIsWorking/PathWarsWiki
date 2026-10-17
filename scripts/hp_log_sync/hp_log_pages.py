"""Publish every campaign's HP and Stamina log from the ComeOnOverUno server as one wiki page per campaign.

Added 2026-10-17. Tongs Browser posts every HP or Stamina change on a player character to the server, which keeps
them; ``GET api/pathwars/campaigns/<code>/hp-history`` returns them anonymously (Lewis ruled 2026-09-28 that a
player character's HP is the table's). The hourly workflow runs this.

⭐ **The server's record is the source of truth.** Each ``<code>-HP-And-Stamina-Log.md`` (in the campaign's own
folder), the index under ``topics/HP-And-Stamina-Logs/`` and the whole of ``hp-logs.tree`` are generated and
overwritten. Only campaigns with any history get a page.

⛔ **A failed fetch never removes a page.** A campaign whose history could not be read keeps the page it had; only
a campaign the server answers for with no changes at all loses one. A server older than ``hp-history`` (404) is
read as "nothing recorded yet".

Idempotent: a run that changes nothing writes nothing.
"""

import argparse
import importlib.util
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from xml.sax.saxutils import quoteattr

sys.path.insert(0, str(Path(__file__).resolve().parent))
from hp_log_render import page_name, render_page  # noqa: E402


def _load_guard():
    """pbp_sync's whole-wiki duplicate guard, loaded by path (see encounter_pages.py for why not by import)."""
    path = Path(__file__).resolve().parent.parent / "pbp_sync" / "guards.py"
    spec = importlib.util.spec_from_file_location("pbp_sync_guards", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.assert_no_duplicate_topics


assert_no_duplicate_topics = _load_guard()

DEFAULT_SERVER = "https://cooserver.duckdns.org"
START_PAGE = "HP-And-Stamina-Logs.md"
WIKI_ROOT = Path(__file__).resolve().parent.parent.parent
TOPICS_DIR = WIKI_ROOT / "Writerside" / "topics"
INDEX_DIR = TOPICS_DIR / "HP-And-Stamina-Logs"
TREE_PATH = WIKI_ROOT / "Writerside" / "hp-logs.tree"
CAMPAIGN_DIR = re.compile(r"^(C\d{2})-(.+)$")


class FetchFailed(Exception):
    pass


def campaign_folders(topics_dir: Path) -> dict[str, Path]:
    """code -> the campaign's folder: the one holding a page named after itself ("C06-Kibwe/C06-Kibwe.md"),
    else the first by name. C01 has three folders; its main one is C01-Doomsday-Funtime."""
    found: dict[str, list[Path]] = {}
    for folder in sorted(p for p in topics_dir.iterdir() if p.is_dir()) if topics_dir.exists() else []:
        match = CAMPAIGN_DIR.match(folder.name)
        if match:
            found.setdefault(match.group(1), []).append(folder)
    return {code: next((f for f in folders if (f / f"{f.name}.md").exists()), folders[0])
            for code, folders in found.items()}


def campaign_name(folder: Path) -> str:
    """"C06-Kibwe" -> "Kibwe"."""
    match = CAMPAIGN_DIR.match(folder.name)
    return match.group(2).replace("-", " ") if match else folder.name


def fetch_history(server: str, code: str, opener=urllib.request.urlopen) -> list[dict]:
    """Every change, oldest first, following ``truncated`` pages. 404 is a server without hp-history: none."""
    changes: dict[str, dict] = {}
    since = None
    while True:
        query = "" if since is None else "?" + urllib.parse.urlencode({"since": since})
        url = f"{server.rstrip('/')}/api/pathwars/campaigns/{code}/hp-history{query}"
        request = urllib.request.Request(url, headers={"User-Agent": "PathWarsWiki-hp-log-sync",
                                                       "Accept": "application/json"})
        try:
            with opener(request, timeout=30) as response:
                body = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return []
            raise FetchFailed(f"{code}: HTTP {e.code}") from e
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, UnicodeDecodeError) as e:
            raise FetchFailed(f"{code}: {e}") from e
        page = body.get("changes") if isinstance(body, dict) else None
        if not isinstance(page, list):
            raise FetchFailed(f"{code}: not an hp-history answer")
        before = len(changes)
        for change in page:
            if isinstance(change, dict):
                changes.setdefault(str(change.get("id")), change)
        # ⚠️ ``since`` is inclusive, so a page adds at least one new row or paging would never end.
        if not body.get("truncated") or len(changes) == before or not page:
            break
        since = page[-1].get("at")
    return sorted(changes.values(), key=lambda c: str(c.get("at") or ""))


def render_index(pages: dict[str, tuple[str, list[dict] | None]]) -> str:
    """None for a page kept from an earlier run because this run could not read the campaign."""
    out = ["# HP and Stamina logs", "",
           "Every change to a player character's HP and Stamina, with when and why, one page per campaign. "
           "Recorded by Tongs Browser and kept by the ComeOnOverUno server.", ""]
    if not pages:
        out.append("No HP or Stamina changes recorded yet.")
    for code, (name, changes) in sorted(pages.items()):
        if changes is None:
            out.append(f"- [{code} {name}]({page_name(code)}): not refreshed in the latest run")
            continue
        latest = str(changes[-1].get("at") or "")[:10]
        out.append(f"- [{code} {name}]({page_name(code)}): {len(changes)} change(s), latest {latest}")
    return "\n".join(out).rstrip("\n") + "\n"


def render_tree(codes: list[str]) -> str:
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<!DOCTYPE instance-profile',
           '        SYSTEM "https://resources.jetbrains.com/writerside/1.0/product-profile.dtd">', "",
           "<!-- GENERATED by scripts/hp_log_sync - do not edit by hand. -->", "",
           f'<instance-profile id="hp-logs" name="HP and Stamina logs" start-page="{START_PAGE}">',
           f'    <toc-element topic="{START_PAGE}">']
    out += [f"        <toc-element topic={quoteattr(page_name(code))}/>" for code in sorted(codes)]
    out += ["    </toc-element>", "</instance-profile>"]
    return "\n".join(out) + "\n"


def _write(path: Path, body: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == body:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8", newline="\n")
    return True


def sync(fetch, topics_dir: Path = TOPICS_DIR, index_dir: Path = INDEX_DIR, tree_path: Path = TREE_PATH):
    """Write each campaign's page, the index and the tree. Returns (files changed, campaigns that failed)."""
    folders = campaign_folders(topics_dir)
    pages: dict[str, tuple[str, list[dict] | None]] = {}
    failed: list[str] = []
    changed = 0
    for code, folder in sorted(folders.items()):
        name = campaign_name(folder)
        try:
            changes = fetch(code)
        except FetchFailed as e:
            print(f"::warning::Could not read {code}'s HP history, so its page is left as it was: {e}")
            failed.append(code)
            if (folder / page_name(code)).exists():
                pages[code] = (name, None)
            continue
        path = folder / page_name(code)
        if changes:
            changed += _write(path, render_page(code, name, changes))
            pages[code] = (name, changes)
        elif path.exists():
            path.unlink()
            changed += 1
    changed += _write(index_dir / START_PAGE, render_index(pages))
    changed += _write(tree_path, render_tree(list(pages)))
    assert_no_duplicate_topics(topics_dir)
    return changed, failed


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--server", default=DEFAULT_SERVER, help="the ComeOnOverUno server")
    args = parser.parse_args(argv)
    changed, failed = sync(lambda code: fetch_history(args.server, code))
    print(f"HP and Stamina logs: {changed} file(s) changed; {len(failed)} campaign(s) unreadable.")
    # Every campaign unreadable is the server being down, worth a red run; one or two is a warning.
    return 1 if failed and len(failed) == len(campaign_folders(TOPICS_DIR)) else 0


if __name__ == "__main__":
    sys.exit(main())
