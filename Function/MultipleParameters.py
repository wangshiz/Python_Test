# 位置参数：调用函数时 根据函数定义的参数位置来传递参数
def userinfo(name, age, gender):
    print(f'名字{name} + 年龄{age} + 性别{gender}')

# 传递参数和定义的参数顺序及个数必须一致
userinfo('tom', 20, '男')

# 关键字传参 函数调用时 通过 'key:value' 形式传递参数
userinfo(name="小谬", age=20, gender='男')
# 位置可变化
userinfo(age=20, gender='男',name="小谬")
# 可以和位置参数混用，位置参数必须在前，且匹配参数顺序
userinfo('小秒', gender= '女', age= 30)

# 缺省参数：声明方法时给参数设置默认值 所有位置参数必须出现再默认参数前，包括函数定义和调用
def userinfo(name, age, gender = '男'):
    print(f'名字{name} + 年龄{age} + 性别{gender}')

userinfo(name="小谬", age=20)
userinfo(name="小谬", age=20, gender='女')

# 不定长参数：
# 位置传递 会作为元组存在 接收不定长数量的参数传入
def userinfo(*args):
    print(type(args))
    print(args)

userinfo(1, 2, 20, '女')

# 关键字传递 会作为字典存在
def userinfo(**kwargs):
    print(type(kwargs))
    print(kwargs)

userinfo(name='tom', age=20, gender='女')

# 其他的看DynamicReference.py



