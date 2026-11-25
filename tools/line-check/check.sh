#!/usr/bin/env bash
# Check every line. Exit 1 if a proven/untested line has a problem, or a known_bad line passes.
set -euo pipefail
cd "$(dirname "$0")"
cue vet -c=false . 
cue export . -e report --out json | python3 -c '
import json, sys
r = json.load(sys.stdin); bad = 0
for name, l in r.items():
    v = l["violations"]; st = l["status"]
    ok = (not v) if st != "known_bad" else bool(v)
    bad += not ok
    print(("PASS" if ok else "FAIL"), f"[{st}]", name)
    for x in v: print("   -", x)
sys.exit(1 if bad else 0)'
