#!/usr/bin/env python3
import sys

max_word = None
max_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        _, value = line.split('\t')
        word, count = value.split('\t')
        count = int(count)
        if count > max_count:
            max_count = count
            max_word = word
    except ValueError:
        continue

# Emit the global maximum
if max_word is not None:
    print(f"{max_word}\t{max_count}")
