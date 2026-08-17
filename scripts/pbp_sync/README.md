# pbp_sync — publishing the play-by-post archive

Copies the PathWarsNudge bot's transcript archive into this wiki as a
Writerside instance.

**The bot's repo is the source of truth.** Everything under
`Writerside/topics/Play-by-posts/Transcripts/` and the whole of
`Writerside/pbp.tree` are generated. An edit made there survives until
the next sync and no longer. To correct a transcript, fix it in
`telegram-pbp-reminder/data/pbp_logs/`.

## What was already true

The bot has been archiving **every** play-by-post message since
**2023-08** — 173 monthly files across 11 campaign directories, roughly
79,000 lines. Nothing needed to start; this only publishes it.

## Running it by hand

```bash
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/LewisIsWorking/telegram-pbp-reminder.git /tmp/botrepo
cd /tmp/botrepo && git sparse-checkout set data/pbp_logs config.json && cd -

python scripts/pbp_sync/sync.py \
  --source /tmp/botrepo/data/pbp_logs \
  --config /tmp/botrepo/config.json
```

Idempotent — a run that changes nothing writes nothing. `.github/workflows/sync-pbp-transcripts.yml`
does the same twice a day and commits only on a real change.

## What the pages look like

Message headers are rewritten. The archive stores

    **Ryo Yamakawa** (2026-08-15 07:51:12) msg#172171@40585:

which repeats the date the day heading already gave, the seconds nobody
needs, and thirteen digits of ids. Published, that becomes

    **Ryo Yamakawa** · 07:51 · [↗](https://t.me/Path_Wars/40585/172171)

⭐ The id is not dropped, it is **spent**: those two numbers are exactly
what a `t.me` deep link needs, so the noisiest part of the line becomes
the one thing the wiki could not otherwise offer — a jump straight to the
message. Ids only exist from 2026, so earlier lines render without a link
rather than with a broken one.

⚠️ **Only headers change.** Prose, images, week and day headings all pass
through byte for byte, and `test_only_header_lines_differ` pins that.

## Layout

    Transcripts/
      PBP-Transcripts.md          master index, the instance start page
      C06-Kibwe-PBP-Index.md      one per campaign: months, counts, voices
      2023/ 2024/ 2025/ 2026/     the transcripts themselves

Year folders are for humans browsing the repo; Writerside resolves topics
by bare filename and does not care where they sit.

## The trap worth knowing about

⛔ **Writerside resolves `.tree` topics by bare filename**, recursively
across `topics/`. The source archive is `<Campaign>/<YYYY-MM>.md`, so ten
campaigns each own a file called `2026-08.md`. Copied across unchanged,
Writerside would point every reference at whichever twin it found first,
publishing one month and silently hiding nine — with no error.

Every published page is therefore named
`<code>-<Campaign>-PBP-<YYYY-MM>.md`, and `sync` refuses to write at all
if two pages would share a name.

## Campaign mapping

Derived from the bot's `config.json` (`topic_pairs[].name` → `code`), so a
new campaign maps itself. Finished campaigns that have left the config
are listed in `naming.RETIRED`.

A directory that matches neither **stops the sync**. That is deliberate:
a campaign whose history quietly fails to publish is worse than a run
that fails loudly. Checking both directions is what surfaced C10
(configured, no transcripts yet) and `Dark_Pockets` / `Magni_Watch`
(transcripts, no config).

## Tests

```bash
python -m pytest scripts/pbp_sync -q
```

21 tests. Two of them (`test_the_collision_guard_can_fail`,
`test_the_mapping_guard_can_fail`) exist to prove the other guards can
actually fail.

## Known limits

- **Message IDs only exist from 2026 onward.** Earlier entries carry name
  and timestamp but no `msg#<id>@<thread>` marker, because the archiver
  added them in 2026. Nothing can backfill them.
- Writerside itself is not built here — the toolchain is not available in
  CI, so `pbp.tree` is checked structurally rather than compiled.
