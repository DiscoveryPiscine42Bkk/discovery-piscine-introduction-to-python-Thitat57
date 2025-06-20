#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print("none")
    sys.exit()

num = 0
while (num <= 10):
    start = 0
    print(f"Table de {num}: ", end="")
    while (start <= 10):
        end_string = "\n" if start == 10 else " "
        if (start == 10): end_string = "\n"
        print(f"{num * start}", end=end_string)
        start += 1
    num += 1
