
def define_tuple():
    a = (1)  # 这里的（）只代表运算顺序
    print(type(a))  # <class 'int'>

    b = (1,)
    print(type(b))  # <class 'tuple'>

    # 结论: 
    #    如果声明元组的时候只有一个元素，结尾要加","


def init_dict_zip():
    print("\n", "使用zip返回元组")
    a = [
        'a,1',
        'a,2',
        'a,3'
    ]
    b = [
        'b,1',
        'b,2',
        'b,3',
        'b,4'
    ]
    for i in zip(a, b):  # 返回一个iterable zip object
        print(i)


if __name__ == '__main__':
    define_tuple()
    init_dict_zip()