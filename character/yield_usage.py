# coding: utf8


def big_list():
    for _ in range(1000):
        yield _


# 只有在迭代时 才依次生成元素 减少内存占用
for i in big_list():
    print(i)
