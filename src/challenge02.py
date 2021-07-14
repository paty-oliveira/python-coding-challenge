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
    if len(statement) % 2 == 0:
        return ""
    else:
        return statement[len(statement) // 2]
