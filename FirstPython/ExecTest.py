a = input("请为func(a)函数添加打印内容")
s2 = input("现在请调用func(a)函数")

s = "def func(a):"+a+"\n"+s2

exec(s)
