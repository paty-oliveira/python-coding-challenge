import unittest
from src.challenge20 import zap


class TestChallenge20(unittest.TestCase):

    def test_should_return_a_list_with_one_tuple(self):
        input_param1 = [0]
        input_param2 = [10]
        current_result = zap(input_param1, input_param2)
        expected_result = [(0, 10)]

        self.assertEqual(current_result, expected_result)

    def test_should_return_a_list_with_two_tuples(self):
        input_param1 = [0, 1]
        input_param2 = [10, 20]
        current_result = zap(input_param1, input_param2)
        expected_result = [(0, 10), (1, 20)]

        self.assertEqual(current_result, expected_result)

    def test_should_return_a_list_with_three_tuples(self):
        input_param1 = [0, 1, 2]
        input_param2 = [10, 20, 30]
        current_result = zap(input_param1, input_param2)
        expected_result = [(0, 10), (1, 20), (2, 30)]

        self.assertEqual(current_result, expected_result)

    def test_should_return_a_empty_list_when_input_lists_have_different_length(self):
        input_param1 = [1, 2]
        input_param2 = [10]
        current_result = zap(input_param1, input_param2)
        expected_result = []

        self.assertEqual(current_result, expected_result)


if __name__ == '__main__':
    unittest.main()
