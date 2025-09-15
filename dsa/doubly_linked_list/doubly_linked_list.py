from node import Node


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def length(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def display(self):
        current = self.head
        content = ""

        while current is not None:
            content += str(current.get_data()) + "<->"
            current = current.get_next()

        print("NULL" + "<->" + content + "NULL")

    def append(self, data):
        """
        Adds a new node with the given data at the end of the sequence.
        """
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            new_node.set_previous(self.tail)
            self.tail = new_node

    def prepend(self, data):
        """
        Adds a new node with the given data at the beginning of the sequence.
        """
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.head.set_previous(new_node)
            new_node.set_next(self.head)
            self.head = new_node

    def add(self, node, data):
        """
        Inserts a new node with the given data immediately after a specified node.
        """
        current = self.head
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        while current is not None:
            if current.get_data() == node.get_data():
                next_node = current.get_next()
                new_node.set_previous(current)
                new_node.set_next(next_node)
                current.set_next(new_node)

            current = current.get_next()

    def delete(self, data):
        """
        Removes the node that contains the given data.
        Returns the removed node.
        """
        current = self.head
        while current is not None:
            if current.get_data() == data:
                previous_node = current.get_previous()
                next_node = current.get_next()

                if previous_node is None:  # deleting the head
                    self.head = next_node
                    self.head.set_previous(None)

                elif next_node is None:  # deleting the tail
                    self.tail = previous_node
                    self.tail.set_next(None)

                else:  # deleting in the middle
                    previous_node.set_next(next_node)
                    next_node.set_previous(previous_node)

                current.set_next(None)
                current.set_previous(None)

                return current.data

            current = current.get_next()
        return None

    def delete_first(self):
        """
        Remove the first node in the list. Returns the node.
        """
        current = self.head

        if current is None:
            return None
        else:
            next = current.get_next()
            current.set_next(None)
            self.head = next

            return current.get_data()

    def delete_last(self):
        """
        Removes the last node in the list. Return the node
        """
        if self.tail is None:
            return None

        else:
            current = self.tail
            previous = self.tail.get_previous()
            previous.set_next(None)
            self.tail = previous

            return current.get_data()

    def search(self, data):
        """
        Finds and returns the node that contains the given data.
        """
        current = self.head

        while current is not None:
            if current.get_data() == data:
                return current.get_data()
            current = current.get_next()

        return None

    def traverse_forward(self):
        """
        Iterates through the list from head to tail.
        """

        return self.display()

    def traverse_backward(self):
        """
        Iterates through the list from tail to head.
        """
        current = self.tail
        content = ""

        while current is not None:
            content += str(current.get_data()) + "<->"
            current = current.get_previous()

        print("NULL" + "<->" + content + "NULL")
