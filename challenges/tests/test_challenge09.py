import unittest
from src.challenge09 import is_anagram


class TestChallenge09(unittest.TestCase):

    def test_should_return_true_when_two_args_are_equal(self):
        input1 = "l"
        input2 = "l"
        current_result = is_anagram(input1, input2)

        self.assertTrue(current_result)

    def test_should_return_true_when_two_args_have_same_elements(self):
        input1 = "le"
        input2 = "el"
        current_result = is_anagram(input1, input2)

        self.assertTrue(current_result)

    def test_should_return_true_when_two_args_have_same_elements_but_in_different_order(self):
        input1 = "typhoon"
        input2 = "opython"
        current_result = is_anagram(input1, input2)

        self.assertTrue(current_result)

    def test_should_return_false_when_two_args_do_not_have_same_elements(self):
        input1 = "Alice"
        input2 = "Bob"
        current_result = is_anagram(input1, input2)

        self.assertFalse(current_result)

    def test_should_return_true_when_two_args_have_same_elements_but_are_in_lower_and_upper_case(self):
        input1 = "TyPhOon"
        input2 = "oPythoN"
        current_result = is_anagram(input1, input2)

        self.assertTrue(current_result)


if __name__ == '__main__':
    unittest.main()
