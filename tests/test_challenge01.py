import unittest
from src.challenge01 import capital_indexes


class TestChallenge01(unittest.TestCase):
    def test_should_return_zero_index(self):
        input_param = "L"
        expected_result = [0]
        current_result = capital_indexes(input_param)

        self.assertEqual(current_result, expected_result)

    def test_should_return_empty_list(self):
        input_param = "lllsas"
        expected_result = []
        current_result = capital_indexes(input_param)

        self.assertEqual(current_result, expected_result)

    def test_should_return_two_indexes_as_capital(self):
        input_param = "TeSt"
        expected_result = [0, 2]
        current_result = capital_indexes(input_param)

        self.assertEqual(current_result, expected_result)

    def test_should_return_three_indexes(self):
        input_param = "HeLlO"
        expected_result = [0, 2, 4]
        current_result = capital_indexes(input_param)

        self.assertEqual(current_result, expected_result)


if __name__ == '__main__':
    unittest.main()
