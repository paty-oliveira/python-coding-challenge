"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

"""


def obtain_high_scoring_word(phrase: str):
    score = {word: sum([ord(letter) - 96 for letter in word])
             for word in phrase.split(" ")}

    return max(score, key=score.get)
