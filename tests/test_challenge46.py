import unittest
from src.challenge46 import mean_square_error


class TestChallenge46(unittest.TestCase):

    def test_should_calculate_mean_square_error(self):
        self.assertEqual(mean_square_error([1, 2, 3], [4, 5, 6]), 9)

        self.assertEqual(mean_square_error([10, 20, 10, 2], [10, 25, 5, -2]), 16.5)

        self.assertEqual(mean_square_error([0, -1], [-1, 0]), 1)

        self.assertEqual(mean_square_error([10, 10], [10, 10]), 0)


if __name__ == '__main__':
    unittest.main()
