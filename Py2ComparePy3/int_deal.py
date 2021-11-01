def devision():
    # python3
    print(5/2)  # >>2.5 结果都会有小数部分。符号少结果多
    print(5//2) # >>2  // 真除法，结果都只保留整数部分 5//2.0=2.0。符号多结果少

    # python2
    print(5/2)  # >>2
    print(5//2) # >>2

    # 向上取整 返回值为 int
    # math.ceil()
    # 向下取整，返回值为 int，类似使用int()
    # math.floor()