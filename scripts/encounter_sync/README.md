# encounter_sync: Foundry encounters as wiki pages

Added 2026-09-17. Publishes every fight the GM runs in Foundry with Tongs Browser's encounter sync as a
page under the **Encounters** instance.

## Where the facts come from

1. Tongs Browser sends each turn of a Foundry encounter to ComeOnOverUno: its name (the GM's, else the
   scene's navigation name), allies, enemies as players see them, and initiative.
2. ComeOnOverUno logs every health band posted to the combat topic during the fight, by round.
3. The Nudge bot reads that each hour and saves `data/encounters/<code>/<YYYY-MM-DD>-<id>.json` in its
   public repo, as a stub when the fight starts and rewritten until it ends.
4. `sync-pbp-transcripts.yml` pulls those records alongside the transcripts and runs
   `encounter_pages.py`, which writes the pages into its existing sync PR.

**The bot's records are the source of truth.** Everything under `topics/Encounters/` and all of
`encounters.tree` is generated and overwritten. Narration, misses and movement are not in the record:
write those on a hand-written page. Generated pages never touch hand-written ones.

## Running it by hand

```bash
python scripts/encounter_sync/encounter_pages.py --source /tmp/botrepo/data/encounters
```

A missing `data/encounters` means no fights yet: the index says so and nothing fails.

## Traps

- ⛔ **Writerside resolves topics by bare filename across `topics/`.** Pages are named
  `<code>-Combat-<Name>-<YYYY-MM-DD>.md`, two fights sharing that get their id appended, and pbp_sync's
  whole-wiki duplicate guard runs after every write, so a generated page can never silently hide a
  hand-written one.
- ⚠️ **The modules are `encounter_`-prefixed on purpose.** pbp_sync has its own `render` and `sync`
  modules; with plain names, whichever one a test session imported first shadowed the other.

## Tests

```bash
python -m pytest scripts/encounter_sync -q
```
