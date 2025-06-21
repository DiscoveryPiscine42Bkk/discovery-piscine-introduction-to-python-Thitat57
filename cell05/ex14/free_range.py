#!/usr/bin/env python3

import sys

if len(sys.argv) == 3:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except ValueError:
        print("Invalid Input!")
        sys.exit()
    arr = []
    for num in range(start, end+1):
        arr.append(num)
    print(arr)
else:
    print("none")