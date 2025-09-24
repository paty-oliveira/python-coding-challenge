"""
Given a list of numbers and a target value, find all unique pairs of numbers in the list whose
sum equals the target.

Each pair should only appear once, even if the numbers occur multiple times in the list.

>>> values = [1, 1, 2, 2, 6, 7, 1, 2]
>>> target = 8
>>> print(find_pair(values, target))
[(1, 7), (2, 6)]

"""


def find_pair(values, total_sum):
    pairs = set()
    for index in range(len(values)):
        for value in values[index + 1 :]:
            if values[index] + value == total_sum:
                pairs.add((values[index], value))

    return list(pairs)
