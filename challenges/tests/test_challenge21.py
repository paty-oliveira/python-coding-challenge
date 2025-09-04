import unittest
from src.challenge21 import validate


class TestChallenge21(unittest.TestCase):

    def test_should_return_true_when_def_keyword_is_in_input(self):
        input_param = "def"
        current_result = validate(input_param)

        self.assertTrue(current_result)

    def test_should_return_true_when_two_dots_keyword_is_in_input(self):
        input_param = ":"
        current_result = validate(input_param)

        self.assertTrue(current_result)

    def test_should_return_true_when_parenthesis_keyword_is_in_input(self):
        input_param = "( and )"
        current_result = validate(input_param)

        self.assertTrue(current_result)

    def test_should_return_true_when_exists_indentation_in_input(self):
        input_param = "    "
        current_result = validate(input_param)

        self.assertTrue(current_result)

    def test_should_return_true_when_validate_keyword_is_in_input(self):
        input_param = "validate"
        current_result = validate(input_param)

        self.assertTrue(current_result)

    def test_should_return_true_when_return_keyword_is_in_input(self):
        input_param = "return"
        current_result = validate(input_param)

        self.assertTrue(current_result)

    def test_should_return_true_when_all_keywords_are_present_in_input(self):
        input_param = "def validate ( and ):" \
                      "    return "
        current_result = validate(input_param)

        self.assertTrue(current_result)

    def test_should_return_missing_def_when_def_keyword_is_not_in_input(self):
        input_param = "validate ( and ):" \
                      "    return "
        current_result = validate(input_param)
        expected_result = "missing def"

        self.assertEqual(current_result, expected_result)

    def test_should_return_missing_validate_when_keyword_is_not_in_input(self):
        input_param = "def  ( and ):" \
                      "    return "
        current_result = validate(input_param)
        expected_result = "wrong name"

        self.assertEqual(current_result, expected_result)

    def test_should_return_missing_return_when_keyword_is_not_in_input(self):
        input_param = "def validate ( and ):" \
                      "    "
        current_result = validate(input_param)
        expected_result = "missing return"

        self.assertEqual(current_result, expected_result)

    def test_should_return_missing_parenthesis_when_keyword_is_not_in_input(self):
        input_param = "def  validate :" \
                      "    return "
        current_result = validate(input_param)
        expected_result = "missing paren"

        self.assertEqual(current_result, expected_result)

    def test_should_return_two_dots_when_keyword_is_not_in_input(self):
        input_param = "def validate ( and )" \
                      "    return "
        current_result = validate(input_param)
        expected_result = "missing :"

        self.assertEqual(current_result, expected_result)


if __name__ == '__main__':
    unittest.main()
