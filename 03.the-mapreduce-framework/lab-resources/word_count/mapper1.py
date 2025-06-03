#!/usr/bin/env python3
import sys

# Input format: word \t count
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        word, count = line.split('\t')
        print(f"null\t{word}:{count}")
    except ValueError:
        continue  # Skip bad lines
