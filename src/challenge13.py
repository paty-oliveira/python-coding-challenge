"""
    Tic tac toe input
    Here's the backstory for this challenge: imagine you're writing a tic-tac-toe game, where the board looks like this:

    1:  X | O | X
       -----------
    2:    |   |
       -----------
    3:  O |   |

        A   B  C
    The board is represented as a 2D list:

    board = [
        ["X", "O", "X"],
        [" ", " ", " "],
        ["O", " ", " "],
    ]

    Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board.
    To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].

    Your task is to write a function that can translate from strings of length 2 to a tuple (row, column).
    Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting
    of an uppercase letter and a digit.

    Example:
    >> get_row_col("A3")
    >> (2, 0)

"""


def get_row_col(param):
    pass
