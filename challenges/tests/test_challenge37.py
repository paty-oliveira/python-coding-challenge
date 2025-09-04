import unittest
from src.challenge37 import validate


class TestChallenge37(unittest.TestCase):

    def test_should_return_true_when_all_letters_appear_once_time(self):
        word = "abc"
        actual_result = validate(word)

        self.assertTrue(actual_result)

    def test_should_return_false_when_letters_appear_in_different_number(self):
        word = "abcabcd"
        actual_result = validate(word)

        self.assertFalse(actual_result)

    def test_should_return_true_when_all_letters_appear_twice(self):
        word = "abcabc"
        actual_result = validate(word)

        self.assertTrue(actual_result)

    def test_should_retirn_true_when_appear_letters_and_symbols_once_time(self):
        word = "123abc!"
        actual_result = validate(word)

        self.assertTrue(actual_result)


if __name__ == '__main__':
    unittest.main()
