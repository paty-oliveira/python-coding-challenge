# Doubly Linked List

A doubly linked list is a sequential data structure where each node contains data and two pointers:
one to the next node in the sequence and one to the previous node. This two-way link allows for transversal
in both forward and backward directions and enables efficient insertions and deletions compared to
singly linked lists.

Each node has three parts: data field and two pointers: `next` - points to the subsequent node in the sequence -
and `previous` - points to the preceding node.

## Description
- `is_empty()`: Returns True if the list has no nodes, otherwise False.
- `append(data)`: Adds a new node with the given data at the end of the list.
- `prepend(data)`: Adds a new node with the given data at the beginning of the list.
- `add(node, data)`: Inserts a new node with the given data immediately after a specified node.
- `delete(data)`: Removes the first node that contains the given data.
- `delete_first()`: Removes the first node in the list.
- `delete_last()`: Removes the last node in the list.
- `search(data)`: Finds and returns the first node that contains the given data, or None if not found.
- `traverse_forward()`: Iterates through the list from head to tail.
- `traverse_backward()`: Iterates through the list from tail to head.
- `length()`: Returns the number of nodes in the list.
- `display()`: Prints the list’s elements from head to tail (for debugging/visualization).
- `display_reverse()`: Prints the list’s elements from tail to head.
