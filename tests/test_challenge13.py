import unittest
from src.challenge13 import get_row_col


class TestChallenge13(unittest.TestCase):

    def test_should_return_initial_position_on_the_board(self):
        input_param = "A1"
        current_result = get_row_col(input_param)
        expected_result = (0, 0)

        self.assertEqual(current_result, expected_result)

    def test_should_return_second_position_on_the_board(self):
        input_param = "A2"
        current_result = get_row_col(input_param)
        expected_result = (1, 0)

        self.assertEqual(current_result, expected_result)

    def test_should_return_third_position_on_the_board(self):
        input_param = "B2"
        current_result = get_row_col(input_param)
        expected_result = (1, 1)

        self.assertEqual(current_result, expected_result)


if __name__ == '__main__':
    unittest.main()
