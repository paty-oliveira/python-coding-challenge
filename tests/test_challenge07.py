import unittest
from src.challenge07 import add_dots, remove_dots


class TestChallenge07(unittest.TestCase):
    def test_should_add_one_dot(self):
        param_input = "t"
        current_result = add_dots(param_input)
        expected_result = "t"

        self.assertEqual(current_result, expected_result)

    def test_should_add_one_dot_when_param_has_2_elements(self):
        param_input = "te"
        current_result = add_dots(param_input)
        expected_result = "t.e"

        self.assertEqual(current_result, expected_result)

    def test_should_add_two_dots_when_param_has_3_elements(self):
        param_input = "tes"
        current_result = add_dots(param_input)
        expected_result = "t.e.s"

        self.assertEqual(current_result, expected_result)

    def test_should_remove_one_dot(self):
        param_input = "t.e"
        current_result = remove_dots(param_input)
        expected_result = "te"

        self.assertEqual(current_result, expected_result)

    def test_should_remove_two_dots(self):
        param_input = "t.e.s"
        current_result = remove_dots(param_input)
        expected_result = "tes"

        self.assertEqual(current_result, expected_result)

    def test_should_return_same_param_input(self):
        param_input = "test"
        current_result = remove_dots(add_dots(param_input))
        expected_result = param_input

        self.assertEqual(current_result, expected_result)


if __name__ == '__main__':
    unittest.main()
