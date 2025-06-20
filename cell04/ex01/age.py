#!/usr/bin/env python3
import sys

user_input = input("Please tell me your age: ")
try:
    age = int(user_input)
except ValueError:
    print("Invalid Input!")
    sys.exit()
print(f"You are currently {age} years old.")
for i in range(10, 31, 10):
    print(f"In {i} years, you'll be {age + i} years old.")