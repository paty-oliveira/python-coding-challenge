import unittest
from src.challenge06 import double_letters


class TestChallenge06(unittest.TestCase):
    def test_should_return_true_when_param_has_two_letters_equals_in_row(self):
        param_input = "aa"
        current_result = double_letters(param_input)

        self.assertTrue(current_result)

    def test_should_return_false_when_param_has_two_letters_different_in_row(self):
        param_input = "ab"
        current_result = double_letters(param_input)

        self.assertFalse(current_result)

    def test_should_return_false_when_param_has_four_letters_different_in_row(self):
        param_input = "abcd"
        current_result = double_letters(param_input)

        self.assertFalse(current_result)

    def test_should_return_true_when_param_of_three_letters_has_two_letters_equals_in_row(self):
        param_input = "abb"
        current_result = double_letters(param_input)

        self.assertTrue(current_result)

    def test_should_return_false_even_param_has_two_letters_equals_but_not_in_row(self):
        param_input = "nono"
        current_result = double_letters(param_input)

        self.assertFalse(current_result)

    def test_should_return_true_when_param_of_four_letters_has_two_letters_equals_in_row(self):
        param_input = "abbc"
        current_result = double_letters(param_input)

        self.assertTrue(current_result)


if __name__ == '__main__':
    unittest.main()
