#!/usr/bin/env bash
set -uo pipefail
# Local read-only collection. Do not publish raw output to a public repository.
if ! command -v kubectl >/dev/null 2>&1; then echo "kubectl not installed" >&2; exit 2; fi
root="${1:-study-automation/evidence/lab001}"
mkdir -p "$root"
chmod 700 "$root"
run() {
  name="$1"; shift
  printf 'Running %s\n' "$name"
  "$@" >"$root/$name.txt" 2>"$root/$name.stderr"
  code=$?
  printf '%s\n' "$code" >"$root/$name.exitcode"
}
run context kubectl config current-context
run nodes kubectl get nodes -o wide
run pods kubectl get pods -A
run deployments kubectl get deployments -A
run services kubectl get svc -A
run storageclasses kubectl get storageclass
run events kubectl get events -A --sort-by=.lastTimestamp
chmod 600 "$root"/* 2>/dev/null || true
printf '\nCollected locally under %s. Review/redact before sharing.\n' "$root"
