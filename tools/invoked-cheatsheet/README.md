# Invoked cheat sheet generator

Renders the phone cheat sheet images for Writerside/topics/Master-duel/Invoked-practice.md.

1. Edit `LINES`, `INDEX` and `RULES` in `build.py`.
2. Bump `VERSION` and `DATE`.
3. From the repo root: `python3 tools/invoked-cheatsheet/build.py` (needs Python Playwright + Chromium).
4. Images land in `Writerside/images/invoked-cheatsheet/v<VERSION>/`. Update the links and changelog on the practice page.

## Phone page (one link, always latest)

`python3 tools/invoked-cheatsheet/page.py` builds `out/invoked-cheat-sheet.html` from the same data. It is published as a private claude.ai artifact: https://claude.ai/artifact/QN9EBixbg3USELrswv3fw3 . Republish to that URL after each version bump so the link on Lewis's phone stays the same.
