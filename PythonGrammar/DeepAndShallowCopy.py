list1 = ["tim", "sam", "tom", "jerry"]
list2 = list1   # 引用的是内存地址

list2.append("tracy")
print(list2)
print(list1)


# 浅拷贝：copy 创建新对象
list1 = ["a", "b", "c"]
list2 = list1.copy()
list2 = list1[:]    # 切片会产生新的对象
print(id(list1), id(list2))  # 31261640 31306952
list1.append("d")
print(list1)
print(list2)


# list1 = ["a", "b", "c", "d", [1, 2, 3, 4]]
# list2 = list1.copy()
# list1[4].append("e")
# print(list1)
# print(list2)

# 深拷贝
import copy
list1 = ["a", "b", "c", "d", [1, 2, 3, 4]]
list2 = copy.deepcopy(list1)    # 深拷贝，包括内部的所有内容进行拷贝
list1[4].append(6)

print(list1)
print(list2)

"""
为什么要有深浅拷贝？
1.拷贝比创建对象的过程要快
"""

