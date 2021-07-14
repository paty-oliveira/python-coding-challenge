import unittest
from src.challenge05 import only_ints


class TestChallenge05(unittest.TestCase):

    def test_should_return_true_if_two_parameters_are_integers(self):
        param1 = 1
        param2 = 2
        current_result = only_ints(param1, param2)

        self.assertTrue(current_result)

    def test_should_return_false_if_one_parameter_is_not_integer(self):
        param1 = 1
        param2 = "b"
        current_result = only_ints(param1, param2)

        self.assertFalse(current_result)

    def test_should_return_false_if_two_parameters_are_not_integers(self):
        param1 = "asas"
        param2 = "00323dddsd"
        current_result = only_ints(param1, param2)

        self.assertFalse(current_result)


if __name__ == '__main__':
    unittest.main()
