import unittest
from src.challenge36 import convert_to_hex


class TestChallenge36(unittest.TestCase):

    def test_should_return_hexadecimal_representation_of_black(self):
        rgb_code = (0, 0, 0)
        actual_result = convert_to_hex(rgb_code)
        expected_result = "000000"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_hexadecimal_representation_of_red(self):
        rgb_code = (255, 0, 0)
        actual_result = convert_to_hex(rgb_code)
        expected_result = "FF0000"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_hexadecimal_representation_of_green(self):
        rgb_code = (0, 128, 0)
        actual_result = convert_to_hex(rgb_code)
        expected_result = "008000"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_hexadecimal_representation_of_blue(self):
        rgb_code = (0, 0, 255)
        actual_result = convert_to_hex(rgb_code)
        expected_result = "0000FF"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_hexadecimal_representation_of_white(self):
        rgb_code = (255, 255, 255)
        actual_result = convert_to_hex(rgb_code)
        expected_result = "FFFFFF"

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
