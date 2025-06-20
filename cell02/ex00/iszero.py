import sys
#!/usr/bin/env python3

input_text = input()

try:
    number = int(input_text)
except ValueError:
    print("Invalid number!")
    sys.exit()

if (number == 0):
    print("This number is equal to zero.")
else:
    print("This number is different from zero.")