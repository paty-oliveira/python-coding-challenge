class Deque(object):
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        """
        Adds a new item to the front of the deque.
        """
        self.deque.insert(0, item)

    def add_rear(self, item):
        """
        Adds a new item to the end of the deque.
        """

        self.deque.append(item)

    def remove_front(self):
        """
        Removes the front item from the deque.
        @return {item}: The item at the front of the deque, if it is not empty, `None` otherwise.
        """
        return self.deque.pop(0)

    def remove_rear(self):
        """
        Removes the last item from the deque.
        @return {item}: The item at the end of the deque, if it is not empty, `None` otherwise.
        """
        return self.deque.pop()

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.deque)
