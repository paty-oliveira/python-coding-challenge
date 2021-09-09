import unittest
from src.challenge28 import find_missing


class TestChallenge28(unittest.TestCase):

    def test_should_return_the_missing_number_when_input_numbers_have_three_elements(self):
        numbers = [1, 2, 4]
        actual_result = find_missing(numbers)
        expected_result = 3
        self.assertEqual(expected_result, actual_result)

    def test_should_return_the_missing_number_when_input_numbers_have_four_elements(self):
        numbers = [3, 6, 9, 15]
        actual_result = find_missing(numbers)
        expected_result = 12
        self.assertEqual(expected_result, actual_result)

    def test_should_return_the_missing_number_when_input_numbers_have_five_elements(self):
        numbers = [1, 3, 5, 9, 11]
        actual_result = find_missing(numbers)
        expected_result = 7
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
