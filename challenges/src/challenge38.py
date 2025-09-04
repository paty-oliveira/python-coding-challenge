"""
You get an array of arrays.
If you sort the arrays by their length, you will see, that their length-values are consecutive.
But one array is missing!

You have to write a method, that return the length of the missing array.

Example:
[[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3

If the array of arrays is null/nil or empty, the method should return 0.

When an array in the array is null or empty, the method should return 0 too!
There will always be a missing element and its length will be always between the given arrays.
"""


def get_length_of_missing_array(array_of_arrays: list):
    curr_array_length = [len(array) for array in sorted(array_of_arrays, key=len)]
    expect_array_length = [length for length in range(curr_array_length[0], curr_array_length[-1])]
    array_difference = list(set(expect_array_length).difference(set(curr_array_length)))[0]

    return array_difference
