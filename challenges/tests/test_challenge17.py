import unittest
from src.challenge17 import all_equal


class TestChallenge17(unittest.TestCase):

    def test_should_return_true_when_input_has_one_element(self):
        input_param = [1]
        current_result = all_equal(input_param)

        self.assertTrue(current_result)

    def test_should_return_true_when_input_has_two_equals_elements(self):
        input_result = [1, 1]
        current_result = all_equal(input_result)

        self.assertTrue(current_result)

    def test_should_return_false_when_input_has_two_different_elements(self):
        input_result = [1, 2]
        current_result = all_equal(input_result)

        self.assertFalse(current_result)

    def test_should_return_true_when_input_has_three_equals_elements(self):
        input_param = [1, 1, 1]
        current_result = all_equal(input_param)

        self.assertTrue(current_result)

    def test_should_return_false_when_input_has_three_different_elements(self):
        input_param = [1, 2, 4]
        current_result = all_equal(input_param)

        self.assertFalse(current_result)


if __name__ == '__main__':
    unittest.main()
