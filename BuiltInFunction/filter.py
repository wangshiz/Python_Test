"""
筛选函数
语法：filter(function, Iterable)
    function:用来筛选的函数，在filter中会自动的把iterable中的元素传递给function，
然后根据function返回的True或者False来判断是否保留此项数据
    Iterable:可迭代对象
返回一个filter迭代器
"""

lst = ["jetty", "tom", "abiily", "sam", "true", "false"]


# def func(s):
#     return 's' in s


lst2 = filter(lambda s: 's' in s, lst)
print(list(lst2))

lst = [
        {'id': 1, 'name': 'jetty', 'age': 18},
        {'id': 2, 'name': 'alex', 'age': 28},
        {'id': 3, 'name': 'tom', 'age': 20},
        {'id': 4, 'name': 'jerry', 'age': 22},
        {'id': 5, 'name': 'sam', 'age': 24},
        {'id': 6, 'name': 'olico', 'age': 30},
       ]

print(list(filter(lambda s: s["age"] > 25, lst)))
