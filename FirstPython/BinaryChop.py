"""
二分法查找
"""
lst = [21, 22, 23, 24, 25, 26, 27, 28, 29, 210, 211, 213, 214, 215, 216]

n = 217

# 次数
count = 0

# 起始位置
start_len = 0

# 初始位置
end_len = len(lst) - 1

while end_len >= start_len:
    # 中间位置
    middle = (start_len + end_len) // 2
    count += 1
    if n < lst[middle]:
        end_len = middle - 1
    elif n > lst[middle]:
        start_len = middle + 1
    else:
        print("找到这个数{},在{}号位置，{}次找到".format(n, middle + 1, count))
        break
else:
    print("没这个数")

print("#######################################################")

lst = [21, 22, 23, 24, 25, 26, 27, 28, 29, 210, 211, 213, 214, 215, 216]


def binaryChop(lst, start_len, end_len, n, count):
    if end_len < start_len:
        print("不存在")
        return
    middle = (start_len + end_len) // 2
    count += 1
    if n < lst[middle]:
        end_len = middle - 1
    elif n > lst[middle]:
        start_len = middle + 1
    else:
        print("找到这个数{},在{}号位置，{}次找到".format(n, middle + 1, count))
        return
    return binaryChop(lst, start_len, end_len, n, count)


binaryChop(lst, 0, len(lst) - 1, 216, 0)




