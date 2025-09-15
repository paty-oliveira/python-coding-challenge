from doubly_linked_list import DoublyLinkedList
from node import Node

new_list = DoublyLinkedList()
print(new_list.is_empty())  # True
new_list.append("Node 1")
print(new_list.length())  # 1
print(new_list.is_empty())  # False
new_list.append("Node 2")
new_list.append("Node 3")
print(new_list.length())  # 3
new_list.display()  # NULL<->Node 1<->Node 2<->Node 3<->NULL
new_list.prepend("New Head")
new_list.display()  # NULL<->New Head<->Node 1<->Node 2<->Node 3<->NULL
new_node = Node("Node 2")
new_list.add(new_node, "New Node 2")
new_list.display()  # NULL<->New Head<->Node 1<->Node 2<->New Node 2<->Node 3<->NULL
print(new_list.delete("New Node 2"))  # New Node 2
new_list.display()  # NULL<->New Head<->Node 1<->Node 2<->Node 3<->NULL
print(new_list.delete("New Head"))  # New Head
new_list.display()  # NULL<->Node 1<->Node 2<->Node 3<->NULL
print(new_list.search("Node 1"))  # Node 1
print(new_list.search("Not exist"))  # None
print(new_list.search("Node 3"))  # Node 3
print(new_list.delete_first())  # Node 1
new_list.display()  # NULL<->Node 2<->Node 3<->NULL
new_list.append("Node 4")
new_list.append("Node 5")
new_list.display()  # NULL<->Node 2<->Node 3<->Node 4<->Node 5<->NULL
new_list.append("New tail")
print(new_list.length())  # 5
print(new_list.delete_last())  # New tail
new_list.display()  # NULL<->Node 2<->Node 3<->Node 4<->Node 5<->NULL
new_list.traverse_forward()  # NULL<->Node 2<->Node 3<->Node 4<->Node 5<->NULL
print(new_list.length())  # 4
new_list.traverse_backward()  # NULL <->Node 5<->Node 4<->Node 3<->Node 2<->NULL
print(new_list.length())  # 4
