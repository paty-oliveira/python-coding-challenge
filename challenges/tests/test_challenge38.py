import unittest
from src.challenge38 import get_length_of_missing_array


class TestChallenge38(unittest.TestCase):

    def test_should_return_two_as_missing_array_when_arrays_are_sorted(self):
        input_array = [[1], [1, 2, 2]]
        actual_result = get_length_of_missing_array(input_array)
        expected_result = 2

        self.assertEqual(expected_result, actual_result)

    def test_should_return_two_as_missing_array_when_arrays_are_unsorted(self):
        input_array = [[1, 2, 2], [1]]
        actual_result = get_length_of_missing_array(input_array)
        expected_result = 2

        self.assertEqual(expected_result, actual_result)

    def test_should_return_three_as_missing_array_when_arrays_are_unsorted(self):
        input_array = [[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]
        actual_result = get_length_of_missing_array(input_array)
        expected_result = 3

        self.assertEqual(expected_result, actual_result)

    def test_should_return_two_as_missing_array_when_arrays_contain_none_values(self):
        input_array = [[None], [None, None, None]]
        actual_result = get_length_of_missing_array(input_array)
        expected_result = 2

        self.assertEqual(expected_result, actual_result)

    def test_should_return_five_as_missing_array_when_arrays_contains_characters(self):
        input_array = [['a', 'a', 'a'], ['a', 'a'], ['a', 'a', 'a', 'a'], ['a'], ['a', 'a', 'a', 'a','a', 'a']]
        actual_result = get_length_of_missing_array(input_array)
        expected_result = 5

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
