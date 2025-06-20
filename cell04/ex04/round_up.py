#!/usr/bin/env python3

import math

user_input = input("Give me a number: ")
try:
    user_input = float(user_input)
    print(math.ceil(user_input))
except ValueError:
    print("Invalid Input!")