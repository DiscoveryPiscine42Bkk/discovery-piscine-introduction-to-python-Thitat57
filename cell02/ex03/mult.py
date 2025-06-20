#!/home/codespace/.python/current/bin/python3
import sys

first_input = input("Enter the first number:\n")
second_input = input("Enter the second number:\n")

try:
    number1 = int(first_input)
    number2 = int(second_input)
except ValueError:
    print("One or Both arguements are not integers.")
    sys.exit()

mult = number1 * number2
print(f"{number1} x {number2} = {mult}")
if (mult > 0):
    print("The result is positive.")
elif (mult < 0):
    print("The result is negative.")
else:
    print("The result is positive and negative.")
