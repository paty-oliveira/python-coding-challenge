# Stack

A stack is a linear data structure that operates in Last-in, First-out (LIFO) principle, meaning the
last item added to the stack is the first item removed.

## Description

Implement a stack data structure that contains the following operations:

- `Stack()`: Creates an instance of a Stack class that doesn't contain any items. The constructor does not accept any arguments.
- `push()`: Pushes an item onto the top of the stack and returns the new length of the stack. Required time complexity: O(1).
- `pop()`: Removes an item at the top of the stack and returns that item. Required time complexity: O(1).
- `is_empty()`: Determines if the stack is empty. Required time complexity: O(1).
- `peek()`: Returns the item at the top of the stack without removing it from the stack. Required time complexity: O(1).
- `length()`: Returns the number of items in the stack. Required time complexity: O(1).

Examples:

```python
stack = Stack()
stack.is_empty() # true
stack.push(1)
stack.push(2)
stack.length() # 2
stack.push(3)
stack.peek() # 3
stack.pop() # 3
stack.is_empty() # false
```
