import unittest
from src.challenge11 import largest_difference


class TestChallenge11(unittest.TestCase):

    def test_should_return_zero_when_input_param_has_one_element(self):
        input_param = [1]
        current_result = largest_difference(input_param)
        expected_result = 0

        self.assertEqual(current_result, expected_result)

    def test_should_return_1_when_input_param_is_the_following(self):
        input_param = [1, 2]
        current_result = largest_difference(input_param)
        expected_result = 1

        self.assertEqual(current_result, expected_result)

    def test_should_return_2_when_input_param_is_the_following(self):
        input_param = [1, 2, 3]
        current_result = largest_difference(input_param)
        expected_result = 2

        self.assertEqual(current_result, expected_result)

    def test_should_return_negative_number_when_input_param_has_only_negative_numbers(self):
        input_param = [-1, -10, -9, -200]
        current_result = largest_difference(input_param)
        expected_result = 199

        self.assertEqual(current_result, expected_result)


if __name__ == '__main__':
    unittest.main()
