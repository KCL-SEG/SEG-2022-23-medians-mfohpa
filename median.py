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
if len(numbers) % 2 == 1:
    print(numbers[len(numbers) / 2])
else:
    mid1 = len(numbers) // 2
    mid2 = mid1 - 1
    print((numbers[mid1] + numbers[mid2]) / 2)
