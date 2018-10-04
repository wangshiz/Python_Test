"""
排序函数
语法:sorted(Iterable, key=None, reverse=False)
Iterable:可迭代对象
key:排序规则(排序函数)
reverse:排列顺序，是否正序倒序
"""

lst = [5, 7, 6, 12, 334, 43, 12, 61, 12, 8]

lst2 = sorted(lst, reverse=False)  # 返回一个新列表
print(lst2)

# 给列表排序，根据字符串的长度进行排序
lst = ["jetty", "tom", "abiily", "sam", "true", "false"]


# def func(s):
#     return len(s)


ll = sorted(lst, key=lambda s: len(s))  # 内部把可迭代对象中的每一个元素传递给func
print(ll)


lst = [
        {'id': 1, 'name': 'jetty', 'age': 18},
        {'id': 2, 'name': 'alex', 'age': 28},
        {'id': 3, 'name': 'tom', 'age': 20},
        {'id': 4, 'name': 'jerry', 'age': 22},
        {'id': 5, 'name': 'sam', 'age': 24},
        {'id': 6, 'name': 'olico', 'age': 30},
       ]


# def func(dic):
#     return dic['age']


ll = sorted(lst, key=lambda s: s['age'])
print(ll)

