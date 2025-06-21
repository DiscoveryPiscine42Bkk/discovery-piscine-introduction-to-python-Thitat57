#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print(f"parameters: {len(sys.argv) - 1}")
    for i in range(len(sys.argv) - 1):
        print(f"{sys.argv[i + 1]}: {len(sys.argv[i + 1])}")
else:
    print("none")