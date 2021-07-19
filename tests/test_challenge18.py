import unittest
from src.challenge18 import tripple_and


class TestChallenge18(unittest.TestCase):

    def test_should_return_true_when_all_arguments_are_true(self):
        input_param1 = True
        input_param2 = True
        input_param3 = True
        current_result = tripple_and(input_param1, input_param2, input_param3)

        self.assertTrue(current_result)

    def test_should_return_false_when_one_argument_is_false(self):
        input_param1 = False
        input_param2 = True
        input_param3 = True
        current_result = tripple_and(input_param1, input_param2, input_param3)

        self.assertFalse(current_result)

    def test_should_return_false_when_two_arguments_are_false(self):
        input_param1 = True
        input_param2 = False
        input_param3 = False
        current_result = tripple_and(input_param1, input_param2, input_param3)

        self.assertFalse(current_result)

    def test_should_return_false_when_all_arguments_are_false(self):
        input_param1 = False
        input_param2 = False
        input_param3 = False
        current_result = tripple_and(input_param1, input_param2, input_param3)

        self.assertFalse(current_result)


if __name__ == '__main__':
    unittest.main()
