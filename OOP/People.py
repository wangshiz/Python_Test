class People:
    """
    类体:
        变量部分
        方法部分
    """
    height = '66'   # 变量，静态变量，静态字段
    weight = '170'
    character = ''

    def __init__(self, name, age, sex):
        self.name = name    # 给对象添加封装属性
        self.age = age
        self.sex = sex

    def whatToDo(self, a):
        print(self, a)

"""
# 查询
# print(People.__dict__)
# 查询
print(People.name)
# 增
People.money = 100
# 改
People.name = 'tom'
# 删
del People.character
print(People.__dict__)

# 操作类名的方法
People.whatToDo(111)

"""
if __name__ == '__main__':
    a = People(1, 2, 3)
    print(a.__dict__)
    a.weight = 50

    print(a.weight)

    print(People.__dict__)
    People.name = 'ss'
    print(People.name)
    del a.weight
    print(a.name)
    print(People.__dict__)
    print(a.__dict__)

