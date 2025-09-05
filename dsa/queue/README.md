# Queue

A queue is an ordered collection of items where the addition of new items happens at one end,
called the "rear", and the removal of existing items occurs at the other end, commonly called the "front".
This ordering principle is called FIFO (First-In, First-Out).

## Description

Implement a queue data structure in Python that contains the following operations:
- `Queue()`: Creates an instance of a Queue class that doesn't contain any items. The constructor does not accept any arguments.
- `enqueue()`: Adds an item to the back of the queue. Required time complexity: O(1).
- `dequeue()`: Removes an item from the front of the queue. Required time complexity: O(1).
- `isEmpty()`: Determines if the queue is empty. Required time complexity: O(1).
- `front()`: Returns the item at the front of the queue without removing it from the queue. Required time complexity: O(1).
- `back()`: Returns the item at the back of the queue without removing it from the queue. Required time complexity: O(1).
- `length()`: Returns the number of items in the queue. Required time complexity: O(1).

Examples:
```python
queue = Queue()
queue.isEmpty() # true
queue.enqueue(1)
queue.enqueue(2)
queue.length() # 2
queue.enqueue(3)
queue.front() # 1
queue.back() # 3
queue.dequeue() # 1
queue.isEmpty() # false
```