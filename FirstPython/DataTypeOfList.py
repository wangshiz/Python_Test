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

'''
List内置了有很多方法，例如append()、pop()等等，这在后面会讲到。
注意：
1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的。
'''
