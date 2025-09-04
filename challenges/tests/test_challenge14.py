import unittest
from src.challenge14 import palindrome


class TestChallenge14(unittest.TestCase):

    def test_should_return_same_param_input_when_param_input_has_one_letter(self):
        input_param = "a"
        current_result = palindrome(input_param)

        self.assertTrue(current_result)

    def test_should_return_true_when_param_input_is_palindrome_word(self):
        input_param = "bob"
        current_result = palindrome(input_param)

        self.assertTrue(current_result)

    def test_should_return_false_when_param_input_is_not_palindrome_word(self):
        input_param = "hello"
        current_result = palindrome(input_param)

        self.assertFalse(current_result)


if __name__ == '__main__':
    unittest.main()
