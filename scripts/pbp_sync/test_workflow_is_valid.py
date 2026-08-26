"""The sync workflow must parse, and must ask for what it uses.

COVERS  YAML validity of every workflow in this repo, and the specific
        permissions / steps the sync workflow depends on.
MISSES  whether GitHub accepts the semantics. Only a real run proves
        that, and a real run is what found both of the bugs below.
PROVEN  by ``test_the_yaml_check_can_fail``.

────────────────────────────────────────────────────────────────────────

Two bugs in one afternoon, neither findable by reading:

1. ``git sparse-checkout set`` defaults to **cone mode**, which treats
   every argument as a directory. ``config.json`` is a file, so the first
   real run died with *"'config.json' is not a directory"*.

2. The PR body contained a blank line at column 0, which **terminates a
   YAML block scalar**. The file stopped being valid YAML, and nothing
   local would have said so — the workflow simply would not have run.

⭐ A workflow is code that only ever executes somewhere else. It gets no
type checker, no import error, no test run. The cheapest guard available
is "does it parse, and does it ask for the permissions it uses", so that
is what this does. Everything past that needs an actual dispatch.
"""
from pathlib import Path

import pytest

yaml = pytest.importorskip("yaml", reason="pyyaml not installed")

WORKFLOWS = Path(__file__).resolve().parent.parent.parent / ".github" / "workflows"
SYNC = WORKFLOWS / "sync-pbp-transcripts.yml"


def _load(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_every_workflow_parses():
    """The blank-line-at-column-0 bug, caught for any workflow here."""
    if not WORKFLOWS.exists():
        pytest.skip("no workflows directory")
    for path in sorted(WORKFLOWS.glob("*.yml")):
        try:
            assert _load(path), f"{path.name} parsed to nothing"
        except yaml.YAMLError as exc:
            pytest.fail(f"{path.name} is not valid YAML: {exc}")


def test_the_yaml_check_can_fail(tmp_path):
    """Feed the checker the exact shape that broke: a run block whose
    continuation line sits at column 0."""
    bad = tmp_path / "broken.yml"
    bad.write_text(
        'jobs:\n  a:\n    steps:\n      - run: |\n'
        '          echo "start\n'
        '\n'
        'this line ends the block scalar"\n', encoding="utf-8")
    with pytest.raises(yaml.YAMLError):
        yaml.safe_load(bad.read_text(encoding="utf-8"))


def test_sync_workflow_asks_for_the_permissions_it_uses():
    """It pushes a branch and opens a PR. Both need granting explicitly,
    and a missing one fails only at the very end of a real run."""
    perms = _load(SYNC).get("permissions", {})
    assert perms.get("contents") == "write", "it pushes a branch"
    assert perms.get("pull-requests") == "write", "it runs gh pr create"


def test_sync_workflow_tests_before_it_writes():
    """Finding out afterwards that the naming rule regressed means
    reviewing a commit that has already renamed 170+ files."""
    steps = _load(SYNC)["jobs"]["sync"]["steps"]
    names = [s.get("name", "") for s in steps]
    assert names.index("Test the sync logic") < names.index(
        "Publish into the wiki")


def test_sparse_checkout_is_not_in_cone_mode():
    """Cone mode cannot select a file, and this needs config.json.

    Pinned because the failure mode is remote-only: the command is
    perfectly valid, it just silently means something else.
    """
    body = SYNC.read_text(encoding="utf-8")
    assert "sparse-checkout set --no-cone" in body


def test_only_the_policy_failure_is_tolerated():
    """The PR step swallows one named condition and no other.

    "Allow GitHub Actions to create and approve pull requests" is off by
    default, and the branch push — the actual job — has already
    succeeded by then, so failing the run over it would be noise. But a
    step that swallowed EVERY error is how a broken sync reports success
    for a month. The tolerance must be narrow and the error path must
    still exit non-zero.
    """
    body = SYNC.read_text(encoding="utf-8")
    assert "not permitted to create or approve pull requests" in body, (
        "the tolerated condition must be matched by name, not by exit code")
    assert "exit $CODE" in body, "any other failure must still fail the run"
    assert "::error::" in body, "and must be visible as an error"


def test_the_workflow_never_pushes_to_master():
    """master is protected and requires a review. A workflow that tries
    fails at the last step, after doing all the work."""
    body = SYNC.read_text(encoding="utf-8")
    assert "bot/pbp-transcripts" in body
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("git push") and "--force origin" not in stripped:
            pytest.fail(f"unqualified push in the sync workflow: {stripped}")
