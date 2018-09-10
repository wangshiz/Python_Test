"""
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
创建格式：
param = {value01,value02,...}
或者
set(value)
"""
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)      # 自动去掉重复数据
# {'Tom', 'Jim', 'Mary', 'Jack', 'Rose'}

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')
# Rose 在集合中

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)    # {'c', 'r', 'a', 'd', 'b'}

print(a - b)    # a和b的差集    {'r', 'd', 'b'}

print(a | b)    # a和b的并集    {'c', 'l', 'z', 'r', 'a', 'm', 'd', 'b'}

print(a & b)    # a和b的交集    {'a', 'c'}

print(a ^ b)    # a和b中不同时存在的元素  {'d', 'r', 'l', 'm', 'z', 'b'}


