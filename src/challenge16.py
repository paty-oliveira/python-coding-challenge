"""
    Consecutive zeros
    The goal of this challenge is to analyze a binary string consisting of only zeros and ones.
    Your code should find the biggest number of consecutive zeros in the string.
    Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones.
    Your function should return the number described above.

    Example:
    >> consecutive_zeros("1001101000110")
    >> 3
"""

import re


def consecutive_zeros(instructions: str):
    max_zeros = 0
    if instructions.count("0") >= 1:
        max_zeros = max(map(len, re.findall("[0]+", instructions)))

    return max_zeros
