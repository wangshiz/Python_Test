"""
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以 不相同 ，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
列表截取的语法格式如下：
变量[头下标:尾下标]
"""
arr = [123, 'abc', 3, 3.5, True, 'runoob']
tinylist = [123, 'runoob']

print(arr)             # 输出完整列表 [123, 'abc', 3, 3.5, True, 'runoob']
print(arr[0])          # 输出列表的第一个元素 123
print(arr[1:3])        # 从第二个开始输出到下标为3的数为止（但不包含下标为3的值） ['abc', 3]
print(arr[1:-1])       # 从第二个元素输出到倒数第二个元素 ['abc', 3, 3.5, True]
print(arr[2:])         # 从第三个元素开始输出后面所有元素 [3, 3.5, True, 'runoob']
print(tinylist*2)      # 输出两次列表 [123, 'runoob', 123, 'runoob']
print(arr+tinylist)    # 连接list和tinylist两个列表 [123, 'abc', 3, 3.5, True, 'runoob', 123, 'runoob']

arrtest = ['abcd', 786, 2.23, 'runoob', 70.2]
print(arrtest[1:3])
print(arrtest[1:1])
print(arrtest[1:0])
print(arrtest[0:1])
'''
[786, 2.23]
[]
[]
['abcd']
'''

print(arrtest[1:-1])    # 从下标为1的数开始，输出到下标为4但不包含4的所有值
print(arrtest[-3:-2])   # 从下标为2的数开始，输出到下标为3但不包含3的所有值
'''
[786, 2.23, 'runoob']
[2.23]
'''

'''
与Python字符串不一样的是，列表中的元素是可以改变的：
'''
a = [1, 2, 3, 4, 5]
a[0] = 9
a[2:5] = [2312, 4342, 4234]     # 改值
print(a)    # [9, 2, 2312, 4342, 4234]
a[2:5] = []     # 删值
print(a)    # [9 ,2]
a[2:100] = [321, 546, 3366, 3332]
print(a)    # [9, 2, 321, 546, 3366, 3332]
print(a[1:5:2])


lists = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [1, 2]
# 列表长度
print(len(lists))
# 返回列表最大值
print(max(lists))
# 返回列表最小值
print(min(lists))
# list(seq) 元组转列表
# 在列表末尾添加新的对象
lists.append({123, 345})
print(lists)
# 统计某个元素在列表出现次数
print(lists.count({123, 345}))
# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
lists.extend(list2)
print(lists)
# 从列表中找出某个值第一个匹配项的索引位置
print(lists.index(1))
# 将对象插入列表
lists.insert(1, 20)
print(lists)
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(lists.pop(2))
# 移除列表中某个值的第一个匹配项
lists.remove(20)
# 反向列表中元素
lists.reverse()
print(lists)
# 对原列表进行排序
lists.remove({123, 345})
lists.sort()
print(lists)
lists.sort(reverse=True)    # 倒序
# 复制list
list3 = lists.copy()

print(list3)
# 清除list
lists.clear()
lists.extend("abc")     # 迭代添加
# 清除list2 下标为0的值
del list2[0]
# 也可以这样写:   del list2   整个清除
print(lists)
print("list2是", list2)

# 列表的嵌套
list3.append([1, 2, 3])
print(list3)
print(list3[9][2])

arr = ['abc', 'def', 'ghi']
strs = ""
for i in arr:
    strs += (i + "_")
print(strs[:len(strs)-1])
print(strs[:-1])


# 删除列表元素
dic_list = []
list1 = [1, 2, 3, 4]
for i in list1:
    dic_list.append(i)

for i in dic_list:
    list1.remove(i)

print(list1)


lst = [1, 3, 5]
it = reversed(lst)  # 将列表倒序排列  并变成一个迭代器
print(list(it))


lst = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
s = slice(1, 3, 1)  # 切片函数
print(lst[s])


'''
List内置了有很多方法，例如append()、pop()等等，这在后面会讲到。
注意：
1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的。
'''


