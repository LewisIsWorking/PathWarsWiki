# Calls the delegate skill with UTF-8 output, for extract.py.
#
# Without this, pwsh writes to a pipe in the console code page, and the first
# non-ASCII character in a reply (a name like "Bayakan" with its accent, a
# non-breaking space) fails Python's UTF-8 decode and loses the whole month.
param(
    [Parameter(Mandatory)][string] $Task,
    [Parameter(Mandatory)][string] $File
)
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8
& (Join-Path $HOME '.claude/skills/delegate/delegate.ps1') `
    -Task $Task -Files $File -Profile accurate -MaxTokens 16000
exit $LASTEXITCODE
