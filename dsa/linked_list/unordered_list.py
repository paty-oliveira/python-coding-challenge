from node import Node


class UnorderedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            current = current.get_next()
            count += 1

        return count

    def search(self, item):
        current = self.head
        found = False

        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

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

        if previous is None:  # if the item we want is the head/first item
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        """
        Adds a new item to the end of the list making it the last item in the collection.
        It needs the item and returns nothing
        """
        new_node = Node(item)
        current = self.head

        if self.head is None:  # if the list is empty
            self.head = new_node
        else:
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

    def insert(self, pos, item):
        """
        Adds a new item to the list at position pos. It needs the item and returns nothing.
        Assume the item is not already in the list and there are enough existing items to habve
        positions pos.
        """
        current = self.head
        previous = None
        new_node = Node(item)
        count = 0

        if pos == 0:
            new_node.set_next(current)
            self.head = new_node

        else:
            while current is not None:
                if count == pos:
                    new_node.set_next(current)
                    previous.set_next(new_node)
                    break
                else:
                    previous = current
                    current = current.get_next()
                    count += 1

    def index(self, item):
        """
        Returns the position of the item in the list. It needs the item and returns the index.
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
        Removes and returns the last item in the list. It needs nothing and returns an item.
        """
        current = self.head
        previous = None

        if self.head.get_next() is None:
            self.head = None
        else:
            while current is not None:
                if current.get_next() is None:
                    previous.set_next(None)
                    break
                else:
                    previous = current
                    current = current.get_next()

        return current.data
