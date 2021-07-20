"""
    Challenge
    Solution validation
    The aim of this challenge is to write code that can analyze code submissions.
    We'll simplify things a lot to not make this too hard.
    Write a function named validate that takes code represented as a string as its only parameter.

    Your function should check a few things:

    - the code must contain the def keyword
        - otherwise return "missing def"
    - the code must contain the : symbol
        - otherwise return "missing :"
    - the code must contain ( and ) for the parameter list
        - otherwise return "missing paren"
    - the code must not contain ()
        - otherwise return "missing param"
    - the code must contain four spaces for indentation
        - otherwise return "missing indent"
    - the code must contain validate
        - otherwise return "wrong name"
    - the code must contain a return statement
        - otherwise return "missing return"
    If all these conditions are satisfied, your code should return True.
"""


def analyze_code(code):
    return [True for keyword in ["def", ":", "( and )", "    ", "validate", "return"] if keyword in code]


def process_error_messages(code):
    keywords_error_messages = {
        "def": "missing def",
        ":": "missing :",
        "( and )": "missing paren",
        "    ": "missing indent",
        "validate": "wrong name",
        "return": "missing return"
    }
    return [error_message for keyword, error_message in keywords_error_messages.items() if keyword not in code]


def validate(code_statement):
    syntax_checks = analyze_code(code_statement)
    error_messages = process_error_messages(code_statement)

    if len(syntax_checks) == 6:
        return True
    else:
        return error_messages[0]
