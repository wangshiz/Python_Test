"""
判断输入内容有多少个整数。
例如：afadasdsad123sadsadd435das7da8sd   print:4
"""
count = 0
last_num = ""
input_num = input("输入一个字符串")
for i in range(len(input_num)):
    if i == 0:
        if input_num[i].isalpha():
            last_num = input_num[i]
        else:
            count += 1
            last_num = input_num[i]
    else:
        if input_num[i].isalpha():
            last_num = input_num[i]
        else:
            if last_num.isalpha():
                count += 1
                last_num = input_num[i]
            else:
                last_num = input_num[i]

print(count)
