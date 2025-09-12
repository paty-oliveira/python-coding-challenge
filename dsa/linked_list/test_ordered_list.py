from ordered_list import OrderedList

my_list = OrderedList()
my_list.add(1)
my_list.add(3)
my_list.add(2)
my_list.add(4)
print(my_list.size())  # 4
print(my_list.index(1))  # 0
print(my_list.index(2))  # 1
print(my_list.pop())  # 4
my_list.remove(1)
my_list.add(-10)
my_list.add(99)
print(my_list.size())  # 4
my_list.print()
