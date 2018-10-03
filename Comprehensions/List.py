"""
列表推导式
语法：[最终结果 for 变量 in 可迭代对象]
"""

lst = []
for i in range(1, 15):
    lst.append(i)
else:
    print(lst)


lst2 = [i for i in range(1, 15)]
print(lst2)


# 获取100以内能被3整除的数
lst3 = [i for i in range(1, 101) if i % 3 == 0]
print(lst3)

# 100以内能被3整除的数的平方
lst4 = [i**2 for i in range(1, 101) if i % 3 == 0]
print(lst4)

# 寻找下列名字中包含两个e的名字
name = [
    ['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
    ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']
]

lst5 = [j for i in name for j in i if j.count("e") == 2]
print(lst5)

for i in name:
    for j in i:
        if j.count("e") == 2:
            print(j)
