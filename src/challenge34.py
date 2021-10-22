"""
You will be given an array of numbers. You have to sort the odd numbers in ascending
order while leaving the even numbers at their original positions.

Examples
    [7, 1]  =>  [1, 7]
    [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""


def sort_by_odd_numbers(numbers: list) -> list:
    sorted_odd_numbers = sorted([number for number in numbers if number % 2 != 0])
    indexes_odd_numbers = [index for index, number in enumerate(numbers) if number % 2 != 0]

    for index in indexes_odd_numbers:
        numbers[index] = sorted_odd_numbers.pop(0)

    return numbers

