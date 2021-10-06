import unittest
from src.challenge32 import encode_rot13


class TestChallenge32(unittest.TestCase):

    def test_should_return_an_empty_result_when_phrase_is_empty(self):
        word = ""
        actual_result = encode_rot13(word)
        expected_result = ""

        self.assertEqual(expected_result, actual_result)

    def test_should_return_one_encoded_letter_by_rot13_cipher(self):
        word = "a"
        actual_result = encode_rot13(word)
        expected_result = "n"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_one_simple_word_by_rot13_cipher(self):
        word = "hello"
        actual_result = encode_rot13(word)
        expected_result = "uryyb"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_one_word_with_special_characters(self):
        word = "hello!"
        actual_result = encode_rot13(word)
        expected_result = "uryyb!"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_one_word_with_numbers(self):
        word = "hello1"
        actual_result = encode_rot13(word)
        expected_result = "uryyb1"

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
