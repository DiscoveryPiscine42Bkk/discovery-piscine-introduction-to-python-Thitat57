#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    for c in sys.argv[1]:
        if (c == 'z'):
            print(c, end="")
    print()
else:
    print("none")