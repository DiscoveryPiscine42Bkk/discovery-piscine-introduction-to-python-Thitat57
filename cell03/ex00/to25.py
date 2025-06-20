#!/usr/bin/env python3
import sys

text_input = input("Enter a number less than 25\n")
try:
    number = int(text_input)
except ValueError:
    print("Invalid Input!")
    sys.exit()

if (number > 25):
    print("Error")
    sys.exit()

while (number <= 25):
    print(f"Inside the loop, my variable is {number}")
    number += 1