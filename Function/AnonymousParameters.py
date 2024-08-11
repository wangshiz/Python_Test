# 匿名函数
def add(compute):
    result = compute(1, 2)
    print(result)

add(lambda x, y: x * y)
add(lambda x, y, z: x * y * z)