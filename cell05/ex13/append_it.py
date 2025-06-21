#!/usr/bin/env python3

import sys, re

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        if not re.search(r"ism$", arg):
            print(arg + "ism")
else:
    print("none")