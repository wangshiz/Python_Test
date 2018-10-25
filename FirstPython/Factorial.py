"""
阶乘
"""
# num 数字，从num开始
# sum 总和


def factorial(num, sum):
    if num == 1:
        return sum
    else:
        sum1 = sum * num
        return factorial(num - 1, sum1)


result = factorial(0, 1)
print(result)