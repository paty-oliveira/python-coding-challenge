from node import Node


class OrderedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            current = current.get_next()
            count += 1

        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True

            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()

        else:
            previous.set_next(current.get_next())

    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        new_node = Node(item)
        if previous is None:  # if the list has one item
            new_node.set_next(self.head)
            self.head = new_node
        else:
            new_node.set_next(current)
            previous.set_next(new_node)

    def index(self, item):
        """
        Returns the position of item in the list. It needs the item and returns the index.
        Assume the item is in the list.
        """
        current = self.head
        pos = 0

        while current is not None:
            if current.get_data() == item:
                return pos
            else:
                current = current.get_next()
                pos += 1

    def pop(self):
        """
        Removes and returns the item at position pos. It needs the position and returns the item.
        Assume the item is in the list.
        """
        current = self.head
        previous = None

        while current is not None:
            if current.get_next() is None:
                previous.set_next(None)
                return current.get_data()
            else:
                previous = current
                current = current.get_next()

    def print(self):
        """
        Prints the list content.
        """
        current = self.head
        content = ""

        while current is not None:
            content += str(current.get_data()) + "->"
            current = current.get_next()

        print(content + "NULL")
