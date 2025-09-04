"""
    Min-maxing
    Define a function named largest_difference that takes a list of numbers as its only parameter.
    Your function should compute and return the difference between the largest and smallest number in the list.
    You may assume that no numbers are smaller or larger than -100 and 100.

    Example:
    >> largest_difference([1, 2, 3])
    >> 2
"""


def largest_difference(numbers):
    return max(numbers) - min(numbers)
