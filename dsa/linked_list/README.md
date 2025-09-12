# Linked List

A linked list is a linear collection of data elements whose order is not given by their physical
placement in memory. Instead, each element points to the next. It's a data structure consisting of
a collection of nodes which together represent a sequence.

The basic building block for the linked list is the **node**. Each node object must hold at
least two pieces of information. First, the node must contain the list item itself - **data** field.
In addition, each node must hold a reference to the next node.

## Description

Implement a unordered linked list data structure in Python that contains the following operations:
- `List()`: creates a new list that is empty. It needs no parameters and returns an empty list.
- `add(item)`: adds a new item to the list. It needs the item and returns nothing. Assume the item is not already in the list.
- `remove(item)`: removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.
- `search(item)`: searches for the item in the list. It needs the item and returns a boolean value.
- `is_empty()`: tests to see whether the list is empty. It needs no parameters and returns a boolean value.
- `size()`: returns the number of items in the list. It needs no parameters and returns an integer.
- `append(item)`: adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list.
- `index(item)`: returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.
- `insert(pos,item)`: adds a new item to the list at position pos. It needs the item and returns nothing. Assume the item is not already in the list and there are enough existing items to have position pos.
- `pop()`: removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.
- `pop(pos)` removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.
