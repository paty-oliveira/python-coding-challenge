import unittest
from src.challenge35 import move_zeros


class TestChallenge35(unittest.TestCase):

    def test_should_return_the_same_numbers_when_not_exists_zeros(self):
        numbers = [1, 2, 1, 2, 1]
        actual_result = move_zeros(numbers)
        expected_result = [1, 2, 1, 2, 1]

        self.assertEqual(expected_result, actual_result)

    def test_should_return_zeros_in_the_end_of_the_list(self):
        numbers = [0, 1, 2, 1, 2]
        actual_result = move_zeros(numbers)
        expected_result = [1, 2, 1, 2, 0]

        self.assertEqual(expected_result, actual_result)

        numbers = [0, 1, 2, 0, 1, 2]
        actual_result = move_zeros(numbers)
        expected_result = [1, 2, 1, 2, 0, 0]

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
