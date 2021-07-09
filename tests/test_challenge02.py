import unittest
from src.challenge02 import mid


class TestChallenge02(unittest.TestCase):
    def test_should_return_empty_string_when_parameter_is_empty(self):
        input_param = ""
        expected_result = ""
        current_result = mid(input_param)

        self.assertEqual(current_result, expected_result)

    def test_should_return_middle_letter_when_parameter_size_is_3(self):
        input_param = "abc"
        expected_result = "b"
        current_result = mid(input_param)

        self.assertEqual(current_result, expected_result)

    def test_should_return_empty_string_when_parameter_size_is_4(self):
        input_param = "aaaa"
        expected_result = ""
        current_result = mid(input_param)

        self.assertEqual(current_result, expected_result)

    def test_should_return_middle_letter_when_parameter_size_is_5(self):
        input_param = "abcde"
        expected_result = "c"
        current_result = mid(input_param)

        self.assertEqual(current_result, expected_result)

    def test_should_return_middle_letter_when_parameter_size_is_11(self):
        input_param = "abcdefghijk"
        expected_result = "f"
        current_result = mid(input_param)

        self.assertEqual(current_result, expected_result)


if __name__ == '__main__':
    unittest.main()
