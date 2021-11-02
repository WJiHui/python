# encoding:utf-8

"""
删去列表中指定的项
"""
def del_target_1(words, target):
    k = 0
    for i in range(len(words)):
        i -= k
        if words[i] == target:
            k += 1
            words.remove(words[i])
    print(words)
    
def del_target_2(words, target):
    # 使用words[:]新copy一份，会产生新的的内存
    [words.remove(i) for i in words[:] if i == target]
    print(words)

def del_target_3(words, target):
    # 逆序循环，pop是删除最左边的元素，下面继续向左遍历，长度减少，但是下标没有混乱
    for i in range(len(words)-1, -1, -1):
        if words[i] == target:
            words.pop(i)
    print(words)

def del_target_4(words, target):
    # 计算次数删除
    for i in range(words.count(target)):
        words.remove(target)
    print(words)


def main():
    del_target_1(['a', 'b', 'c', 'c', 'e', 'a', 'b'], target='a')
    del_target_2(['a', 'b', 'c', 'c', 'e', 'a', 'b'], target='a')
    del_target_3(['a', 'b', 'c', 'c', 'e', 'a', 'b'], target='a')
    del_target_4(['a', 'b', 'c', 'c', 'e', 'a', 'b'], target='a')


if __name__ == '__main__':
    main()

