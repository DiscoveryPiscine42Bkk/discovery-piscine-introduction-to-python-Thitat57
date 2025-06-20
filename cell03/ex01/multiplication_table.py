import sys
#!/usr/bin/env python3

text_input = input("Enter a number\n")
try:
    number = int(text_input)
except ValueError:
    print("Invalid Input!")
    sys.exit()

start = 0
while (start <= 12):
    print(f"{start} x {number} = {start*number}")
    start += 1