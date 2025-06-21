#!/usr/bin/env python3

import sys

def shrink(string):
    print(string[:8])
def enlarge(string):
    while len(string) < 8:
        string += 'Z'
    print(string)

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        else:
            enlarge(arg)
else:
    print("none")