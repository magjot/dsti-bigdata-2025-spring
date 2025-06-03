#!/usr/bin/env python3
import sys

# Just forward data with the same key
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    print(f"null\t{line}")
