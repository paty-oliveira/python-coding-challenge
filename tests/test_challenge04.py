import unittest
from src.challenge04 import random_number


class TestChallenge04(unittest.TestCase):
    def test_should_return_an_integer(self):
        current_result = random_number()
        expected_type = int

        self.assertIsInstance(current_result, expected_type)

    def test_should_return_a_number_less_than_100(self):
        current_result = random_number()

        self.assertLessEqual(current_result, 100)


if __name__ == '__main__':
    unittest.main()
