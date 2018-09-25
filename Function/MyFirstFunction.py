def simple_function():
    print("这个是一个简单的方法")
    return "sam"


def second_function():
    print("123")
    return "sam", "jerry", "tom"


def third_function(choice, age):
    print("open %s" % choice)
    print("age %s" % age)
    return


def forth_function(id, name, sex="男"):  # 默认值参数，定义一个方法时先写位置参数再写默认值参数
    print(id, name, sex)


a = simple_function()
print(a)
b = second_function()   # 多个数据返回元组
print(b)
third_function("QQ", 18)    # 位置参数
third_function(choice="WEIXIN", age=19)     # 关键字参数
third_function("QQ", age=20)    # 混合参数  先写位置参数  再写关键字参数
forth_function(1, "xiaoming")
forth_function(2, "xiaohong", "女")
