"""
Fibonacci sequence
斐波那契數列:
    除了第一，第二位数之外后面的数都是前两个数之和
"""
from inspect import isgeneratorfunction


def fibonacci(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n = n + 1

# a = fibonacci(7)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())


print(isgeneratorfunction(fibonacci))   # True

for n in fibonacci(7):
    print(n)

# 当函数执行结束时，generator 自动抛出 StopIteration 异常，表示迭代完成。
# 在 for 循环里，无需处理 StopIteration 异常，循环会正常结束。
