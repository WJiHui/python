
def list_copy():
    a = [1,2,3,4]
    b = a.copy()
    print(b)

    # py3没有问题，list可以直接copy()
    
    # py2执行这段代码报错，list不能直接复制
    '''
    AttributeErrorTraceback (most recent call last)
    <ipython-input-1-71ae065418c6> in <module>()
          2 # py3没有问题，list可以直接copy()
          3 a = [1,2,3,4]
    ----> 4 b = a.copy()
          5 print(b)

    AttributeError: 'list' object has no attribute 'copy'
    '''
    
def list_copy_ok():
    # py2和py3通用copy方法
    import copy
    a = [1,2,3,4]
    b = copy.copy(a)     # 浅拷贝
    b = copy.deepcopy(a) # 深拷贝，用于a是复杂字典情况下
    print(b)
