"""
    Palindrome
    A string is a palindrome when it is the same when read backwards.
    Write a function named palindrome that takes a single string as its parameter.
    Your function should return True if the string is a palindrome, and False otherwise.

    Example:
    >> palindrome("bob")
    >> True
    >> palindrome("hello")
    >> False
"""


def palindrome(word):
    return word == word[::-1]
