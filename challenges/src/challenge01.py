"""
    Capital indexes
    Write a function named capital_indexes.
    The function takes a single parameter, which is a string.
    Your function should return a list of all the indexes in the string that have capital letters.

    Example:
    >> capital_indexes("HeLlO")
    >> [0, 2, 4]
"""


def capital_indexes(statement: str):
    return [statement.index(letter) for letter in statement if letter.isupper()]
