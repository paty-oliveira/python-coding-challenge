"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

    move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(numbers: list) -> list:
    new_list = [number for number in numbers if number != 0]
    new_list.extend([0] * numbers.count(0))

    return new_list


