"""
    Anagrams
    Write a function named is_anagram that takes two strings as its parameters.
    Your function should return True if the strings are anagrams, and False otherwise.

    Example:
    >> is_anagram("typhoon", "opython")
    >> True
    >> is_anagram("Alice", "Bob")
    >> False
"""


def is_anagram(statement1: str, statement2: str):
    return sorted(statement1.lower()) == sorted(statement2.lower())
