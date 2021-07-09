"""
    Middle Letter
    Write a function named mid that takes a string as its parameter.
    Your function should extract and return the middle letter.
    If there is no middle letter, your function should return the empty string.

    Example:
    >> mid("abc")
    >> "b"
    >> mid("aaaa")
    >> ""
"""


def mid(statement):
    length_statement = len(statement)

    if length_statement % 2 == 0:
        middle_letter = ""
    else:
        index = length_statement // 2
        middle_letter = statement[index]
    return middle_letter
