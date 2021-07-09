"""
    Online Status
    Write a function named online_count that takes one parameter.
    The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
    Your function should return the number of people who are online.

    For example, consider the following dictionary:
    statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
    }
    >> online_count(statuses)
    >> 2
"""


def online_count(statuses: dict):
    online_users = 0
    for status in statuses.values():
        if status == "online":
            online_users += 1
        else:
            online_users = 0

    return online_users
