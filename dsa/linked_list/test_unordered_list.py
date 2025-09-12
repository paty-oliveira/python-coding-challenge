from unordered_list import UnorderedList

my_list = UnorderedList()
print(my_list.is_empty())
my_list.add("Element 1")
my_list.add("Element 2")
print(my_list.is_empty())
print(my_list.size())  # 2
my_list.add("22")
print(my_list.search("22"))  # True
print(my_list.search("not found"))  # False
print(my_list.remove("22"))
print(my_list.search("22"))  # False
my_list.append("last_item")
print(my_list.size())  # 3
my_list.insert(0, "new head")
print(my_list.head.data)  # new head
print(my_list.size())  # 4
my_list.insert(1, "new pos 1 element")
print(my_list.size())  # 5
print(my_list.index("new head"))  # 0
print(my_list.index("new pos 1 element"))  # 1
print(my_list.pop())  # last_item
print(my_list.size())  # 4
