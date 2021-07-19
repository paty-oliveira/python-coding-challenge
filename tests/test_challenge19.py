import unittest
from src.challenge19 import convert


class TestChallenge19(unittest.TestCase):

    def test_should_return_a_list_with_one_converted_string(self):
        input_param = [1]
        current_result = convert(input_param)
        expected_result = ["1"]

        self.assertEqual(current_result, expected_result)

    def test_should_return_a_list_with_two_converted_strings(self):
        input_param = [1, 2]
        current_result = convert(input_param)
        expected_result = ["1", "2"]

        self.assertEqual(current_result, expected_result)

    def test_should_return_a_list_with_three_converted_strings(self):
        input_param = [1, 2, 3]
        current_result = convert(input_param)
        expected_result = ["1", "2", "3"]

        self.assertEqual(current_result, expected_result)


if __name__ == '__main__':
    unittest.main()
