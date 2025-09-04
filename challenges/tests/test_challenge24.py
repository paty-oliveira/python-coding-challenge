import unittest
from src.challenge24 import format_number


class TestChallenge24(unittest.TestCase):

    def test_should_return_a_string_with_one_comma_separator_in_thousands(self):
        input_param = 1000
        current_result = format_number(input_param)
        expected_result = "1,000"

        self.assertEqual(current_result, expected_result)

    def test_should_return_a_string_with_two_comma_separators_in_thousands(self):
        input_param = 1000000
        current_result = format_number(input_param)
        expected_result = "1,000,000"

        self.assertEqual(current_result, expected_result)


if __name__ == '__main__':
    unittest.main()
