import unittest
from src.challenge34 import sort_by_odd_numbers


class TestChallenge34(unittest.TestCase):

    def test_should_sort_all_odd_numbers_in_ascending_order(self):
        numbers = [7, 1, 3]
        actual_result = sort_by_odd_numbers(numbers)
        expected_result = [1, 3, 7]

        self.assertEqual(expected_result, actual_result)

    def test_should_sort_only_the_odd_numbers_keeping_the_even_in_same_position(self):
        numbers = [5, 8, 6, 3, 4]
        actual_result = sort_by_odd_numbers(numbers)
        expected_result = [3, 8, 6, 5, 4]

        self.assertEqual(expected_result, actual_result)

        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        actual_result_result = sort_by_odd_numbers(numbers)
        expected_result = [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

        self.assertEqual(expected_result, actual_result_result)


if __name__ == '__main__':
    unittest.main()
