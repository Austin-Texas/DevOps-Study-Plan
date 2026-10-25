#!/usr/bin/env python3
"""Validate LAB-001 collection completeness; not cluster health."""
from pathlib import Path
import sys
REQUIRED = ("context", "nodes", "pods", "deployments", "services", "storageclasses", "events")
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 lab001_validate.py DIRECTORY"); return 2
    root = Path(sys.argv[1])
    errors = []
    for item in REQUIRED:
        code = root / f"{item}.exitcode"
        output = root / f"{item}.txt"
        if not code.is_file() or not output.is_file():
            errors.append(f"{item}: missing output/exit code")
            continue
        if code.read_text(encoding="utf-8").strip() != "0":
            errors.append(f"{item}: kubectl exited nonzero")
        elif not output.read_text(encoding="utf-8").strip():
            errors.append(f"{item}: empty output")
    for message in errors: print("FAIL", message)
    if errors: return 1
    print("PASS: collection complete; human health review still required")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
