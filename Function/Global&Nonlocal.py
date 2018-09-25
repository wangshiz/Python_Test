a = 10
def function():
    global a    # 用到的是全局a
    a = a + 10
    print(a)

function()
print(a)