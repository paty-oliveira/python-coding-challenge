def binary_search(items, item):
    first = 0
    last = len(items) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if items[midpoint] == item:
            found = True
        else:
            if item < items[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found
