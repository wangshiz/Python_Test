a = 10


def function():
    global a    # 用到的是全局a
    a = a + 10
    print(a)


function()
print(a)

# 20 20
a = 10


def fun2():
    a = 20

    def fun3():
        nonlocal a  # 不取本地的参数  也不取全局参数
        a = 2
        print(a)
    fun3()


fun2()
print(a)
