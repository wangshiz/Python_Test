"""
只读文件
"""

'''
读取一个文件
'''
f = open("./singer", mode="r", encoding="utf-8")
s = f.read()
f.close()   # 关闭句柄
print(s)    # 周杰伦，蔡依林，林俊杰，Aimer，FallOut Boy，TS，侃爷

'''
按行读取
'''
f = open("./eating", mode="r", encoding="utf-8")
s1 = f.readline()
s2 = f.readline()
f.close()   # 关闭句柄
print(s1)   # 炸酱面
print(s2)   # 炸鸡

'''
for循环读取
'''
f = open("./eating", mode="r", encoding="utf-8")
for k, line in enumerate(f):  # 每次读取一行，循环打印所有
    if k == 5:
        print(line)
f.close()   # 关闭句柄


'''
strip()去空格的用法
'''
f = open("./eating", mode="r", encoding="utf-8")
for line in f:
    print(line.strip())     # 去掉空格 还能去掉 \n \t

f.close()   # 关闭句柄

'''
路径问题：
    1.绝对路径
        1)从磁盘根目录寻找
        2)互联网上的一个绝对路径
    2.相对路径
        相对路径，相对于你当前程序所在的文件夹
        ../ 返回上一层目录
        ./  同一层目录
'''