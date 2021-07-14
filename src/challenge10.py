"""
    Flatten a list
    Write a function that takes a list of lists and flattens it into a one-dimensional list.
    Name your function flatten. It should take a single parameter and return a list.

    Example:
    >> flatten([[1, 2], [3, 4]])
    >> [1, 2, 3, 4]
"""


def flatten(two_dimensional_list: list):
    return [element for lists in two_dimensional_list for element in lists]
