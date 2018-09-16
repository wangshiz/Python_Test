"""
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。如果出现相同则后面那个key值会覆盖之前的key值。
"""
dicts = {}
pass
dicts['one'] = '1'
dicts[2] = '2'
dicts['one'] = '4'
print(dicts)    # {'one': '4', 2: '2'}

dit = dict()
dit[0] = 20
print(dit)      # {0: 20}

tinydict = {'name': 'runoob', 'code':1, 'site': 'www.runoob.com'}
print(tinydict)             # {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(tinydict.keys())      # dict_keys(['name', 'code', 'site'])
print(tinydict.values())    # dict_values(['runoob', 1, 'www.runoob.com'])
'''
构造函数 dict() 可以直接从键值对序列中构建字典如下：
'''
dit1 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(dit1)     # {'Runoob': 1, 'Google': 2, 'Taobao': 3}
dit2 = {x: x**2 for x in (2, 4, 6)}
print(dit2)     # {2: 4, 4: 16, 6: 36}
dit3 = dict(Runoob=1, Google=2, Taobao=3)
print(dit3)     # {'Runoob': 1, 'Google': 2, 'Taobao': 3}


dit.setdefault(1, 21)
dit.setdefault(1, 22)   # 无效 因为这个字典里包含了key为1的值
dit[0] = 23     # 赋值
print(dit)
"""
另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。
注意：
1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。
"""
