#!/usr/bin/env bash
# Install CUE v0.11.1 (the version the line checker uses) into ~/.local/bin. Takes about 1 second.
# Order: already installed -> release binary from GitHub -> go install (slow, ~1-2 min).
set -euo pipefail
VER=v0.11.1
if command -v cue >/dev/null 2>&1 || [ -x "$HOME/.local/bin/cue" ]; then exit 0; fi
mkdir -p "$HOME/.local/bin"
case "$(uname -s)-$(uname -m)" in
  Linux-x86_64) P=linux_amd64 ;; Linux-aarch64) P=linux_arm64 ;;
  Darwin-arm64) P=darwin_arm64 ;; Darwin-x86_64) P=darwin_amd64 ;; *) P="" ;;
esac
if [ -n "$P" ]; then
  T=$(mktemp -d)
  if curl -fsSL -o "$T/cue.tgz" "https://github.com/cue-lang/cue/releases/download/$VER/cue_${VER}_${P}.tar.gz" \
     && tar xzf "$T/cue.tgz" -C "$T" cue; then
    mv "$T/cue" "$HOME/.local/bin/cue"; rm -rf "$T"; exit 0
  fi
  rm -rf "$T"
fi
echo "Release download failed; trying go install (slow)..." >&2
GOBIN="$HOME/.local/bin" go install "cuelang.org/go/cmd/cue@$VER"
