# inventory_sync

Publishes the Path Wars Nudge bot's daily inventory snapshots (`data/inventories/<code>/<YYYY-MM-DD>.json` in
`telegram-pbp-reminder`) as one wiki page per campaign under `Writerside/topics/Inventories/`, with its own
Writerside instance (`inventories.tree`). Added 2026-10-17 so a GM can check when any item or currency appeared.

- `inventory_render.py`: one campaign's page. "Now" lists every party and character; "Changes by day" diffs each
  pair of consecutive snapshots.
- `inventory_pages.py`: loads the snapshots, writes the pages, index and tree, and removes pages no snapshot backs.
- `test_inventory_sync.py`: run by the sync workflow before it publishes anything.

## Learnings

- 2026-10-17: items are matched by name and type, not id. Foundry gives an item a new id each time it moves between
  sheets, so an id diff would turn every stash hand-out into a loss plus an unexplained gain. A gain that matches a
  loss on another sheet the same day is reported as a move; only the remainder reads as gained or lost.
