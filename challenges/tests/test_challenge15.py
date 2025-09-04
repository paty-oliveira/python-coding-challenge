import unittest
from src.challenge15 import up_down


class TestChallenge15(unittest.TestCase):

    def test_should_return_zero_as_lower_number_and_2_as_higher_number(self):
        input_param = 1
        current_result = up_down(input_param)
        expected_result = (0, 2)

        self.assertEqual(current_result, expected_result)

    def test_should_return_four_as_lower_number_and_six_as_higher_number(self):
        input_param = 5
        current_result = up_down(input_param)
        expected_result = (4, 6)

        self.assertEqual(current_result, expected_result)

    def test_should_return_minus_2_as_lower_number_and_zero_as_higher_number(self):
        input_param = -1
        current_result = up_down(input_param)
        expected_result = (-2, 0)

        self.assertEqual(current_result, expected_result)


if __name__ == '__main__':
    unittest.main()
