# Linked List

A linked list is a linear collection of data elements whose order is not given by their physical
placement in memory. Instead, each element points to the next. It's a data structure consisting of
a collection of nodes which together represent a sequence.

The basic building block for the linked list is the **node**. Each node object must hold at
least two pieces of information. First, the node must contain the list item itself - **data** field.
In addition, each node must hold a reference to the next node.

## Description

The structure of an unordered list is a collection of items where each item holds a relative position
with respect to the others:

Implement a unordered linked list data structure in Python that contains the following operations:
- `UnorderedList()`: creates a new list that is empty. It needs no parameters and returns an empty list.
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


The structure of an ordered list is a collection of items where each item holds a relative position that
is based upon underlying characteristic of the item. The ordering is typically either ascending or descending
and we assume that list items have a meaningful comparison operation that is already defined. Many of the
ordered list operations are the same as those of the unordered list.

Implement a ordered linked list data structure in Python that contains the following operations:
- `OrderedList()`: creates a new ordered list that is empty. It needs no parameters and returns an empty list.
- `add(item)`: adds a new item to the list making sure that the order is preserved. It needs the item and returns nothing. Assume the item is not already in the list.
- `remove(item)`: removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.
- `search(item)`: searches for the item in the list. It needs the item and returns a boolean value.
- `is_empty()`: tests to see whether the list is empty. It needs no parameters and returns a boolean value.
- `size()`: returns the number of items in the list. It needs no parameters and returns an integer.
- `index(item)`: returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.
- `pop()`: removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.
- `pop(pos)`: removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.
