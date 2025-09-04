"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

  Examples
  "the-stealth-warrior" gets converted to "theStealthWarrior"

  "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

  "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

"""


def to_camel_case(text: str) -> str:
    cleaned_text = text.replace("_", " ").replace("-", " ").split(" ")
    camel_case = list(cleaned_text[0]) + [
        letter.capitalize() for letter in cleaned_text[1:]
    ]

    return "".join(camel_case)
