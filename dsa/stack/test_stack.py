from stack import Stack

new_stack = Stack()
print(new_stack.is_empty())
new_stack.push(1)
new_stack.push(5)
print(new_stack.length())
new_stack.push(3)
print(new_stack.peek())
print(new_stack.pop())
print(new_stack.is_empty())
