def test(x, y):
    print(x - y)

# 相当于测试方法 别的文件导入这个包并运行，这个test方法不会执行
if __name__ == '__main__':
    test(1, 2)
