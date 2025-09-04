import unittest
from src.challenge44 import is_isogram


class TestChallenge44(unittest.TestCase):

    def test_identifies_isogram_words(self):
        isogram_words = ["Dermatoglyphics", "isogram", ""]

        for word in isogram_words:
            actual_result = is_isogram(word)
            self.assertTrue(actual_result)

    def test_identifies_non_isogram_words(self):
        non_isogram__words = ["aba", "moOse", "isIsogram"]

        for word in non_isogram__words:
            actual_result = is_isogram(word)
            self.assertFalse(actual_result)


if __name__ == '__main__':
    unittest.main()
