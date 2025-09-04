"""
    Boolean and
    Define a function named triple_and that takes three parameters
    and returns True only if they are all True and False otherwise.

    Example:
    >> tripple_and(True, True, True)
    >> True
    >> tripple_and(False, True, True)
    >> False
"""


def tripple_and(param1, param2, param3):
    return all([param1, param2, param3])
