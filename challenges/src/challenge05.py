"""
    Type Check
    Write a function named only_ints that takes two parameters.
    Your function should return True if both parameters are integers, and False otherwise.

    Example:
    >> only_ints(1, 2)
    >> True

    >> only_ints("a", 1)
    >> False
"""


def only_ints(param1, param2):
    return isinstance(param1, int) & isinstance(param2, int)
