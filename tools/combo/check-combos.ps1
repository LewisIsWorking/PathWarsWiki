# 2026-08-10: Validates every Crystron combo route against the Master Duel ruleset, in BOTH the
# CUE and the Pkl model, and DIFFS their findings.
#
# Why two models. Keeping one would be less work. The reason for two is that a checker which
# silently under-reports is worse than no checker, because it manufactures confidence - and CUE
# was caught doing exactly that during the bake-off (see README.md). Running both and requiring
# them to AGREE means each one polices the other: the day either silently stops checking
# something, the diff goes red instead of the suite going quietly green.
#
# Exit code 0 = everything agrees and the real routes are clean.
param([switch]$Verbose)

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$fail = @()
$notes = @()

function Need-Tool($name) {
  if (-not (Get-Command $name -ErrorAction SilentlyContinue)) {
    throw "$name is not on PATH. CUE: https://cuelang.org  Pkl: https://pkl-lang.org (drop pkl.exe in ~/.local/bin)"
  }
}
Need-Tool 'cue'
Need-Tool 'pkl'

# 2026-08-10: Route pairs. A route must exist in BOTH models or the diff is meaningless, so a
# missing counterpart is itself a failure rather than a silent skip.
$routes = @(
  @{ name = 'inclusion';      pkl = 'RouteInclusion.pkl';      cue = 'route_inclusion.cue';       expr = 'routeInclusion';      expect = 0 }
  @{ name = 'blue-traveler';  pkl = 'RouteBlueTraveler.pkl';   cue = 'route_blue_traveler.cue';   expr = 'routeBlueTraveler';   expect = 0 }
  @{ name = 'schedule';       pkl = 'RouteSchedule.pkl';       cue = 'route_schedule.cue';        expr = 'routeSchedule';       expect = 0 }
  @{ name = 'smiger';         pkl = 'RouteSmiger.pkl';         cue = 'route_smiger.cue';          expr = 'routeSmiger';         expect = 0 }
  @{ name = 'babeldecker';    pkl = 'RouteBabeldecker.pkl';    cue = 'route_babeldecker.cue';     expr = 'routeBabeldecker';    expect = 0 }
  @{ name = 'flying-launcher';pkl = 'RouteFlyingLauncher.pkl'; cue = 'route_flying_launcher.cue'; expr = 'routeFlyingLauncher'; expect = 0 }
  # 2026-08-10: 12 -> 13 when R3b (a Normal Summon must come from the hand) was added, since the
  # fixture's step 2 normal summons from the DECK. Then 13 -> 14 when step 9 added an ALTERNATE
  # summon under the lock, which CUE had been skipping.
  @{ name = 'broken';         pkl = 'RouteBroken.pkl';         cue = 'route_broken.cue';          expr = 'routeBroken';         expect = 14 }
)

# 2026-08-10: Every finding is diffed, with nothing excluded.
#
# An earlier version of this file excluded zone findings from the diff, on the belief that CUE
# could not fold state across a sequence. That was wrong. CUE could not fold it RECURSIVELY -
# a recursive definition either self-references (silently applying one step) or trips the
# `structural cycle` detector - but INDEXED accumulation works, and now produces findings
# identical to Pkl's. See cue/combo.cue. If an exclusion ever reappears here it needs the same
# burden of proof, because an excluded check is an unchecked check.

function Get-PklErrors($file) {
  $json = pkl eval -f json $file 2>&1 | Out-String
  if ($LASTEXITCODE -ne 0) { throw "pkl failed on $file`n$json" }
  return @(($json | ConvertFrom-Json).route.errors)
}

function Get-CueErrors($expr) {
  $files = @(Get-ChildItem "$root\cue" -Filter '*.cue' | ForEach-Object { $_.FullName })
  $json = & cue export @files -e "$expr.errors" 2>&1 | Out-String
  if ($LASTEXITCODE -ne 0) { throw "cue failed on $expr`n$json" }
  return @($json | ConvertFrom-Json)
}

Write-Host "== combo routes ==" -ForegroundColor Cyan
foreach ($r in $routes) {
  $pklFile = Join-Path "$root\pkl" $r.pkl
  $cueFile = Join-Path "$root\cue" $r.cue
  if (-not (Test-Path $pklFile)) { $fail += "route '$($r.name)': missing Pkl model $($r.pkl)"; continue }
  if (-not (Test-Path $cueFile)) { $fail += "route '$($r.name)': missing CUE model $($r.cue)"; continue }

  $p = Get-PklErrors $pklFile
  $c = Get-CueErrors $r.expr

  # The ratchet. A fixture that stops reporting its planted problems is a broken guard.
  if ($p.Count -ne $r.expect) {
    $fail += "route '$($r.name)': Pkl reported $($p.Count) problems, expected exactly $($r.expect)"
  }

  $pSorted = @($p | Sort-Object)
  $cSorted = @($c | Sort-Object)
  $onlyPkl = @($pSorted | Where-Object { $cSorted -notcontains $_ })
  $onlyCue = @($cSorted | Where-Object { $pSorted -notcontains $_ })

  if ($onlyPkl.Count -or $onlyCue.Count) {
    $fail += "route '$($r.name)': the two models DISAGREE"
    $onlyPkl | ForEach-Object { $fail += "    only Pkl: $_" }
    $onlyCue | ForEach-Object { $fail += "    only CUE: $_" }
  } else {
    Write-Host ("  {0,-12} both models agree, {1} findings" -f $r.name, $pSorted.Count) -ForegroundColor Green
  }

  if ($Verbose) { $p | ForEach-Object { Write-Host "    - $_" -ForegroundColor DarkGray } }
}

# 2026-08-11: Tie the models to the PROSE. Until now the checker validated routes that no reader
# ever sees, while the wiki page could say anything. This closes half that gap: every modelled
# route must be named on the combo page, so deleting or renaming a route without touching the page
# fails. It does NOT verify the steps match - the page is prose and the model is data - so treat
# this as a drift alarm rather than a proof of agreement.
Write-Host "== models vs prose ==" -ForegroundColor Cyan
$prosePage = Join-Path $root '..\..\Writerside\topics\Master-duel\Crystron-trains\Crystron-trains-combos.md'
if (-not (Test-Path $prosePage)) {
  $fail += "combo page not found at $prosePage"
} else {
  # Matched on the model FILENAME rather than the route's display name. A display name is prose and
  # drifts for harmless reasons; a filename is an identifier, so the link stays exact and a rename
  # on either side breaks the build loudly. Same reasoning as identifying by name, never by recency.
  $prose = Get-Content $prosePage -Raw
  $unnamed = @()
  foreach ($r in $routes) {
    if ($r.name -eq 'broken') { continue }  # a fixture, deliberately not in the prose
    if ($prose -notmatch [regex]::Escape($r.pkl)) {
      $unnamed += "route '$($r.name)' is modelled in $($r.pkl) but that model is not cited on the combo page"
    }
  }
  if ($unnamed.Count) { $unnamed | ForEach-Object { $fail += $_ } }
  else { Write-Host "  every modelled route is cited on the combo page" -ForegroundColor Green }
}

# 2026-08-10: Folder README rule, scoped to this tool. A README must exist and NAME EVERY FILE in
# its directory - presence alone is a property of the file, accuracy is a property of its
# relationship to the directory, and only the second catches a file nobody documented.
Write-Host "== folder READMEs ==" -ForegroundColor Cyan
foreach ($dir in @($root, "$root\cue", "$root\pkl")) {
  $readme = Join-Path $dir 'README.md'
  if (-not (Test-Path $readme)) { $fail += "missing README.md in $dir"; continue }
  $text = Get-Content $readme -Raw
  if ($text.Length -lt 400) { $fail += "README.md in $dir is too short to be useful ($($text.Length) chars)" }
  $missing = @(Get-ChildItem $dir -File | Where-Object { $_.Name -ne 'README.md' } | Where-Object { $text -notmatch [regex]::Escape($_.Name) })
  if ($missing.Count) { $missing | ForEach-Object { $fail += "README.md in $dir does not name $($_.Name)" } }

  # 2026-08-10: The other half of the rule. Naming every file catches an UNDOCUMENTED file;
  # it does not catch a file that was DELETED while the README kept describing it. That gap was
  # real - cue/README.md went on naming zonefold.cue after the file was removed, and this check
  # passed. A backticked bare filename (no path separator) must exist in this directory.
  $named = [regex]::Matches($text, '`([A-Za-z0-9_.-]+\.(?:cue|pkl|ps1|md|json))`') | ForEach-Object { $_.Groups[1].Value } | Sort-Object -Unique
  $stale = @($named | Where-Object { -not (Test-Path (Join-Path $dir $_)) })
  if ($stale.Count) { $stale | ForEach-Object { $fail += "README.md in $dir names $_ which does not exist" } }

  if (-not $missing.Count -and -not $stale.Count) {
    Write-Host ("  {0} names all its files, no stale entries" -f (Split-Path $dir -Leaf)) -ForegroundColor Green
  }
}

Write-Host ""
$notes | ForEach-Object { Write-Host "note: $_" -ForegroundColor Yellow }
if ($fail.Count) {
  Write-Host "FAILED:" -ForegroundColor Red
  $fail | ForEach-Object { Write-Host "  $_" -ForegroundColor Red }
  exit 1
}
Write-Host "All combo checks passed." -ForegroundColor Green
exit 0
