#!/usr/bin/env python3

user_input = input("Give me a number: ")
try:
    user_input = float(user_input)
    if user_input.is_integer(): print("This number is an integer.")
    else: print("This number is a decimal.")
except ValueError:
    print("Invalid Input!")