import unittest
from src.challenge16 import consecutive_zeros


class TestChallenge16(unittest.TestCase):

    def test_should_return_zero_consecutive_zeros(self):
        input_param = "1111"
        current_result = consecutive_zeros(input_param)
        expected_result = 0

        self.assertEqual(current_result, expected_result)

    def test_should_return_one_consecutive_zero(self):
        input_param = "1011"
        current_result = consecutive_zeros(input_param)
        expected_result = 1

        self.assertEqual(current_result, expected_result)

    def test_should_return_two_consecutive_zeros(self):
        input_param = "100101"
        current_result = consecutive_zeros(input_param)
        expected_result = 2

        self.assertEqual(current_result, expected_result)

    def test_should_return_three_consecutive_zeros(self):
        input_param = "1001101000110"
        current_result = consecutive_zeros(input_param)
        expected_result = 3

        self.assertEqual(current_result, expected_result)


if __name__ == '__main__':
    unittest.main()
