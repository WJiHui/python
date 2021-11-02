# coding: utf8

def test1():
    def big_list():
        for _ in range(1000):
            yield _  # 循环迭代的时候用yield返回


    # 只有在迭代时 才依次生成元素 减少内存占用
    for i in big_list():
        print(i)



import re

class WordsIter:
    RE_WORD = re.compile('\w+')
    def __init__(self, text):
        self.words = self.RE_WORD.finditer(text)
        print(type(self.words))  # <class 'callable_iterator'>

    def __iter__(self):
        for match in self.words:
            yield match.group()  # 循环迭代的时候用yield返回
        print('iter end')


def test2():    
    s = WordsIter('"The time has come," the Walrus said,')
    
    # 直接遍历words
    for i in s.words:
        print(i.group())
    
    # 使用对象自身的__iter__进行遍历
#     for i in s:
#         print(i)
#     print(next(iter(s))) # StopIteration抛出异常


def test3():
    # Generator 实现惰性执行 (lazy evaluation) ，即在真正需要某个值的时候才真正去计算这个值
    # 一个函数中使用到了yield，这个函数就是一个生成器
    def fibonacci():
        a, b = (0, 1)
        while True:
            yield a  # 每次调用执行到此处，返回a
            a, b = b, a + b  # 下次调用yield 的位置向下执行，继续循环


    fib = fibonacci()
    print(next(fib)) # 0
    print(next(fib)) # 1
    print(next(fib)) # 1
    print(next(fib)) # 2
    print(next(fib)) # 3
    print(next(fib)) # 5


    # next迭代完所有的会抛出StopIteration异常, 
    # 但是这里因为使用了While True条件，next不会永远不会结束