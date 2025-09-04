class Stack(object):
    def __init__(self):
        self.__stack: list = []

    def push(self, item):
        """
        Pushes an item onto the top of the stack.
        @param {*} item: The item to be pushed onto the stack.
        @return {number}: The new length of the stack.
        """

        self.__stack.insert(0, item)

        return self.length()

    def pop(self):
        """
        Remove an item at the top of the stack.
        @return {*}: The item at the top of the stack if it is not empty, `undefined` otherwise.
        """

        return self.__stack.pop(0)

    def is_empty(self):
        """
        Determines if the stack is empty.
        @return {boolean}: `true` if the stack has no items, `false` otherwise.
        """
        return self.length() == 0

    def peek(self):
        """
        Returns the item at the top of the stack without removing it from the stack.
        @return {*}: The item at the top of the stack if it is not empty, `None` otherwise.
        """
        if self.length() == 0:
            return None

        return self.__stack[0]

    def length(self):
        """
        Returns the number of items in the stack.
        @return {number}: The number of items in the stack.
        """
        return len(self.__stack)
