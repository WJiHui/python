

def default_args(a, b={}):
    """
    Default parameter values are evaluated when the function definition is executed.
    This means that the expression is evaluated once, when the function is defined,
    and that same"pre-computed" value is used for each call.
    This is especially important to understand when a default parameter is a mutable object,
    such as a list or a dictionary: if the function modifies the object (e.g. by appending an item to a list),
    the default value is in effect modified.

    函数定义的时候，参数会执行赋值一次，所以一开始就是b就初始化为{},
    其他的语言有些没有这个问题，例如ruby
    b参数应该写成None,然后进行判断后使用
    if b is None:
        b = []
    """
    b[a] = 1
    return b


if __name__ == '__main__':
    print(default_args('a'))  # {'a': 1}
    print(default_args('b'))  # {'a': 1, 'b': 1}
