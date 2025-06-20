#!/usr/bin/env python3
import sys

num1 = input("Give me the first number: ")
num2 = input("Give me the second number: ")
try:
    num1 = int(num1)
    num2 = int(num2)
except ValueError:
    print("Invalid Input!")
    sys.exit()
print("Thank you!")
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
try:
    print(f"{num1} / {num2} = {num1/num2}")
except ZeroDivisionError:
    print(f"Cannot divide {num1} by {num2}")
print(f"{num1} x {num2} = {num1*num2}")