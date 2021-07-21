import unittest
from src.challenge23 import param_count


class TestChallenge23(unittest.TestCase):

    def test_should_return_zero_as_number_of_args(self):
        current_result = param_count()
        expected_result = 0

        self.assertEqual(current_result, expected_result)

    def test_should_return_one_as_number_of_args(self):
        input_param1 = 1
        current_result = param_count(input_param1)
        expected_result = 1

        self.assertEqual(current_result, expected_result)

    def test_should_return_two_as_number_of_args(self):
        input_param1 = 0
        input_param2 = 10
        current_result = param_count(input_param1, input_param2)
        expected_result = 2

        self.assertEqual(current_result, expected_result)

    def test_should_return_three_as_number_of_args(self):
        input_param1 = 1
        input_param2 = 2
        input_param3 = 3
        current_result = param_count(input_param1, input_param2, input_param3)
        expected_result = 3

        self.assertEqual(current_result, expected_result)


if __name__ == '__main__':
    unittest.main()
