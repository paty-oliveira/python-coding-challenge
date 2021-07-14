import unittest
from src.challenge08 import count


class TestChallenge08(unittest.TestCase):

    def test_should_return_zero_syllable(self):
        param_input = "hey"
        current_result = count(param_input)
        expected_result = 1

        self.assertEqual(current_result, expected_result)

    def test_should_return_two_syllables(self):
        param_input = "ho-tel"
        current_result = count(param_input)
        expected_result = 2

        self.assertEqual(current_result, expected_result)

    def test_should_return_three_syllables(self):
        param_input = "ad-vi-ser"
        current_result = count(param_input)
        expected_result = 3

        self.assertEqual(current_result, expected_result)

    def test_should_return_four_syllables(self):
        param_input = "di-rec-to-ry"
        current_result = count(param_input)
        expected_result = 4

        self.assertEqual(current_result, expected_result)


if __name__ == '__main__':
    unittest.main()
