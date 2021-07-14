"""
    Counting syllables
    Define a function named count that takes a single parameter.
    The parameter is a string.
    The string will contain a single word divided into syllables by hyphens.
    Your function should count the number of syllables and return it.

    Example:
    >> count("ho-tel")
    >> 2
"""


def count(statement: str):
    return len([char for char in statement if char == "-"]) + 1
