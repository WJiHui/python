def define_tuple():
    a = (1)  # 这里的（）只代表运算顺序
    print(type(a))  # <class 'int'>

    b = (1,)
    print(type(b))  # <class 'tuple'>

    # 结论: 
    #    如果声明元组的时候只有一个元素，结尾要加","


if __name__ == '__main__':
    define_tuple()
