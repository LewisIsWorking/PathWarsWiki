# Invoked cheat sheet generator

Renders the phone cheat sheet images for Writerside/topics/Master-duel/Invoked-practice.md.

1. Edit `LINES`, `INDEX` and `RULES` in `build.py`.
2. Bump `VERSION` and `DATE`.
3. From the repo root: `python3 tools/invoked-cheatsheet/build.py` (needs Python Playwright + Chromium).
4. Images land in `Writerside/images/invoked-cheatsheet/v<VERSION>/`. Update the links and changelog on the practice page.
