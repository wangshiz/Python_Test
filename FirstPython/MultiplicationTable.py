# 九九乘法表
a = 1
while a <= 9:
    b = 1
    while b <= a:
        print('%d * %d = %d' % (b, a, a * b), end = '\t')
        b += 1
    print()
    a += 1
