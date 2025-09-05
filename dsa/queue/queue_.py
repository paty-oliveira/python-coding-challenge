class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """
        Adds an item to the back of the queue.
        @param {*} item The item to be pushed onto the queue.
        @return {number} The new length of the queue.
        """
        self.queue.append(item)
        return self.length()

    def dequeue(self):
        """
        Removes an item from the front of the queue.
        @return {*} The item at the front of the queue if it is not empty, `None` otherwise.
        """
        return self.queue.pop(0)

    def is_empty(self):
        """
        Determines if the queue is empty.
        @return {boolean} `true` if the queue has no items, `false` otherwise.
        """
        return self.length() == 0

    def front(self):
        """
        Returns the item at the front of the queue without removing it from the queue.
        @return {*} The item at the front of the queue if it is not empty, `undefined` otherwise.
        """
        return self.queue[0]

    def back(self):
        """
        Returns the item at the back of the queue without removing it from the queue.
        @return {*} The item at the back of the queue if it is not empty, `undefined` otherwise
        """
        return self.queue[-1]

    def length(self):
        """
        Returns the number of items in the queue.
        @return {number} The number of items in the queue.
        """
        return len(self.queue)
