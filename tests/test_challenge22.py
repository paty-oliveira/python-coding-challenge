import unittest
from src.challenge22 import list_xor


class TestChallenge22(unittest.TestCase):

    def test_should_return_true_when_one_is_in_first_list(self):
        input_param1 = 1
        input_param2 = [1]
        input_param3 = [0]
        current_result = list_xor(input_param1, input_param2, input_param3)

        self.assertTrue(current_result)

    def test_should_return_true_when_one_is_in_second_list(self):
        input_param1 = 1
        input_param2 = [0]
        input_param3 = [1]
        current_result = list_xor(input_param1, input_param2, input_param3)

        self.assertTrue(current_result)

    def test_should_return_false_when_one_is_in_two_list_simultaneous(self):
        input_param1 = 1
        input_param2 = [1]
        input_param3 = [1]
        current_result = list_xor(input_param1, input_param2, input_param3)

        self.assertFalse(current_result)

    def test_should_return_false_whe_one_is_not_in_any_list(self):
        input_param1 = 1
        input_param2 = [2, 3, 4]
        input_param3 = [5, 6, 7]
        current_result = list_xor(input_param1, input_param2, input_param3)

        self.assertFalse(current_result)


if __name__ == '__main__':
    unittest.main()
