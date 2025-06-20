#!/home/codespace/.python/current/bin/python3
import sys

input_text = input()

try:
    number = int(input_text)
except ValueError:
    print("Invalid number!")
    sys.exit()

if (number > 0):
    print("This number is positive.")
elif (number < 0):
    print("This number is negative.")
else:
    print("This number is both positive and negative.")