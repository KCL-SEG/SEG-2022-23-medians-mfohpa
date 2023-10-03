"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

while len(numbers) > 2:
    numbers.pop()
    numbers.pop(0)

if len(numbers) == 1:
    print(numbers[0])
else:
    print((numbers[0] + numbers[1]) / 2)
