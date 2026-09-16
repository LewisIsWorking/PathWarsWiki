"""Write a campaign's timeline page from its saved scenes. No model involved.

    python scripts/campaign_timeline/page.py \
        --source ../telegram-pbp-reminder/data/pbp_logs/Magni_Guard \
        --data timelines/C04-Magni-Guard.json \
        --page Writerside/topics/C04-The-Magni-Guard/C04-Magni-Guard-Timeline.md

Run it again after filling in ``in_game`` or ``renames`` in the data file.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from messages import read_campaign  # noqa: E402
from page_render import render  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--data", type=Path, required=True)
    p.add_argument("--page", type=Path, required=True)
    p.add_argument("--group", default="Path_Wars")
    a = p.parse_args()
    data = json.loads(a.data.read_text(encoding="utf-8"))
    months = read_campaign(a.source, a.group)
    page = render(data, months, data_file=a.data.as_posix())
    a.page.write_text(page, encoding="utf-8", newline="\n")
    print(f"wrote {a.page}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
