"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
    "camelCasing"  =>  "camel Casing"
    "identifier"   =>  "identifier"
    ""             =>  ""

"""


def break_camel_case(string):
    new_string = ""

    for letter in string:
        if letter.isupper():
            new_string += " " + letter
        else:
            new_string += letter

    return new_string
