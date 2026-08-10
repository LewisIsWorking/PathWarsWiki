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
  @{ name = 'inclusion'; pkl = 'RouteInclusion.pkl'; cue = 'route_inclusion.cue'; expr = 'routeInclusion'; expect = 0 }
  @{ name = 'broken';    pkl = 'RouteBroken.pkl';    cue = 'route_broken.cue';    expr = 'routeBroken';    expect = 12 }
)

# 2026-08-10: A finding is "sequential" when it depends on state accumulated across earlier steps.
# CUE cannot fold state (it returns a wrong answer SILENTLY, proven in the bake-off), so its
# sequential findings are known-unreliable and are reported but NOT diffed. Everything else must
# match exactly. Delete this split the day CUE grows a working fold.
function Is-Sequential($msg) {
  return ($msg -match 'is claimed to act from' -or $msg -match 'is not on the field')
}

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

  $pShared = @($p | Where-Object { -not (Is-Sequential $_) } | Sort-Object)
  $cShared = @($c | Where-Object { -not (Is-Sequential $_) } | Sort-Object)
  $onlyPkl = @($pShared | Where-Object { $cShared -notcontains $_ })
  $onlyCue = @($cShared | Where-Object { $pShared -notcontains $_ })

  if ($onlyPkl.Count -or $onlyCue.Count) {
    $fail += "route '$($r.name)': the two models DISAGREE"
    $onlyPkl | ForEach-Object { $fail += "    only Pkl: $_" }
    $onlyCue | ForEach-Object { $fail += "    only CUE: $_" }
  } else {
    Write-Host ("  {0,-12} agree on {1} shared findings" -f $r.name, $pShared.Count) -ForegroundColor Green
  }

  $pSeq = @($p | Where-Object { Is-Sequential $_ })
  if ($pSeq.Count) { $notes += "route '$($r.name)': $($pSeq.Count) sequential findings (Pkl only, CUE cannot fold state)" }
  if ($Verbose) { $p | ForEach-Object { Write-Host "    - $_" -ForegroundColor DarkGray } }
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
  if (-not $missing.Count) { Write-Host ("  {0} names all its files" -f (Split-Path $dir -Leaf)) -ForegroundColor Green }
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
