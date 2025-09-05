# Deque

A deque, also known as a double-ended queue, is an ordered collections of items similar to the queue.
It has two ends, a front and a rear, and the items remain positioned in the collections. What makes a deque
different is the unrestrictive nature of adding and removing items. New items can be added at either
the front or the rear. Likewise, existing items can be removed from either end. It provides all the capabilities
of stacks and queues in a single data structure.


## Description

Implement a deque data structure in Python that contains the following operations:
- `Deque()`: creates a new deque that is empty. It needs no parameters and returns an empty deque.
- `add_front(item)`: adds a new item to the front of the deque. It needs the item and returns nothing.
- `add_rear(item)`: adds a new item to the end of the deque. It needs the item and returns nothing.
- `remove_front()`: removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
- `remove_rear()`: removes the last item from the deque. It needs no parameters and returns the item. The deque is modified.
- `is_empty()`: determines if the deque is empty. It needs no parameters and returns a boolean value.
- `size()`: returns the number of items in the deque. It needs no parameters and returns an integer.

Examples:
```python
d = Deque()
print(d.isEmpty()) # True
d.addRear(4)
d.addRear('dog')
d.addFront('cat')
d.addFront(True)
print(d.size()) # 4
print(d.isEmpty()) # False
d.addRear(8.4)
print(d.removeRear()) # 8.4
print(d.removeFront()) # True
```
