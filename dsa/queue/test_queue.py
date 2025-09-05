from queue_ import Queue

new_queue = Queue()
print(new_queue.is_empty())
print(new_queue.enqueue("item 1"))
new_queue.enqueue("item 2")
print(new_queue.dequeue())
print(new_queue.is_empty())
new_queue.enqueue("item 3")
print(new_queue.front())
print(new_queue.back())
