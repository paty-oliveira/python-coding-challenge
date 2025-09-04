"""
Write a function that accumulates a letter based on its index position, like the following examples:

>> accum("abcd") -> "A-Bb-Ccc-Dddd"
>> accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
>> accum("cwAt") -> "C-Ww-Aaa-Tttt"

"""


def letter_accum(string):
    acc_string = ""

    for index in range(len(string)):
        first_letter = string[index]
        acc_string += first_letter.upper() + first_letter.lower() * index

        if index != len(string) - 1:
            acc_string += "-"

    return acc_string
