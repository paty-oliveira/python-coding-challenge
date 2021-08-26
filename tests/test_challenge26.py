import unittest
from src.challenge26 import printer_error


class TestChallenge26(unittest.TestCase):

    def test_should_return_zero_errors_when_label_has_letters_from_a_to_m(self):
        input_label = "abcdefghijklm"
        actual_result = printer_error(input_label)
        expected_result = "0/13"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_one_error_when_label_has_one_different_letter_from_control_string(self):
        input_label = "abcdefghixjklm"
        actual_result = printer_error(input_label)
        expected_result = "1/14"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_two_errors_when_label_has_two_different_letters_from_control_string(self):
        input_label = "aabcdefghizz"
        actual_result = printer_error(input_label)
        expected_result = "2/12"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_eight_errors_when_label_has_eight_different_letters_from_control_string(self):
        input_label = "aaaxbbbbyyhwawiwjjjwwm"
        actual_result = printer_error(input_label)
        expected_result = "8/22"

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
