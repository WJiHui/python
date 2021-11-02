# encoding:utf-8

"""
对列表中重复项去重
"""
def remove_duplication_1(words):
    # 需要列表的项都能用作集合的键，可以hashable
    # 速度较快
    print(list(set(words)))

def remove_duplication_2(words):
    # 需要先排序
    words.sort()
    last = words[-1]
    for i in range(len(words)-2, -1, -1):
        if last == words[i]:
            del words[i]
        else:
            last = words[i]
    print(words)

def main():
    words = ['e', 'a', 'd', 'c', 'e', 'a', 'b']
    remove_duplication_1(words)
    remove_duplication_2(words)
if __name__ == '__main__':
    main()

