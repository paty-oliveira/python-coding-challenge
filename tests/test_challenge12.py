import unittest
from src.challenge12 import div_3


class TestChallenge12(unittest.TestCase):

    def test_should_return_true_when_3_is_input_param(self):
        param_input = 3
        current_result = div_3(param_input)

        self.assertTrue(current_result)

    def test_should_return_false_when_2_is_input_param(self):
        param_input = 2
        current_result = div_3(param_input)

        self.assertFalse(current_result)

    def test_should_return_true_when_6_is_input_param(self):
        param_input = 6
        current_result = div_3(param_input)

        self.assertTrue(current_result)


if __name__ == '__main__':
    unittest.main()
