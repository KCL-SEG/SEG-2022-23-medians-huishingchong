"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        numbers.sort() #sort the list
        if len(numbers) > 1:
            median_index = len(numbers)//2
            if len(numbers) % 2 != 0: #odd amount of numbers in list
                print(numbers[median_index])
            else:
                print((numbers[median_index-1] + numbers[median_index])/2)
        else:
            print(numbers[0])
