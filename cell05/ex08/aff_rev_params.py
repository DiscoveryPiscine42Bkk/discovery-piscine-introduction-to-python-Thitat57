#!/usr/bin/env python3

import sys

if (len(sys.argv) < 3):
    print("none")
else:
    for i in range(len(sys.argv) - 1):
        print(sys.argv[len(sys.argv) - i - 1])