"""Lewis, 2026-09-21: "There should be NO em dashes across any repo!"

Zero, over every tracked text file, except the generated transcript pages
under Writerside/topics/Play-by-posts/Transcripts/. Those are verbatim copies
of what people posted in Telegram, made by scripts/pbp_sync, and rewriting
them would falsify the record.
"""

import os
import subprocess

EM_DASH = chr(0x2014)
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_VERBATIM = ("Writerside/topics/Play-by-posts/Transcripts/",)


def _offenders(files, root=_ROOT):
    found = []
    for rel in files:
        if rel.startswith(_VERBATIM):
            continue
        try:
            with open(os.path.join(root, rel), encoding="utf-8") as f:
                for n, line in enumerate(f, 1):
                    if EM_DASH in line:
                        found.append(f"{rel}:{n}")
        except UnicodeDecodeError:
            continue  # binary files (images)
    return found


def _tracked():
    # -z and quotepath off: by default git quotes and escapes non-ASCII paths
    # ("BÃ¡yakan"), open() then fails, and the file is silently skipped.
    out = subprocess.run(["git", "-c", "core.quotepath=off", "ls-files", "-z"], cwd=_ROOT,
                         capture_output=True, text=True, encoding="utf-8", check=True).stdout
    return [f for f in out.split("\0") if f]


def test_there_are_no_em_dashes_outside_the_transcripts():
    found = _offenders(_tracked())
    assert not found, f"{len(found)} line(s) with an em dash: {found[:20]}"


def test_the_guard_can_fail(tmp_path):
    (tmp_path / "x.md").write_text("a " + EM_DASH + " b\n", encoding="utf-8")
    assert _offenders(["x.md"], root=str(tmp_path)) == ["x.md:1"]


def test_the_transcripts_stay_verbatim(tmp_path):
    rel = _VERBATIM[0] + "t.md"
    (tmp_path / rel).parent.mkdir(parents=True)
    (tmp_path / rel).write_text("a " + EM_DASH + " b\n", encoding="utf-8")
    assert _offenders([rel], root=str(tmp_path)) == []
