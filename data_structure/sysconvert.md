# 进制转换 conversion of number systems
- 二进制   binary  0b开头
- 八进制   oct     0o开头
- 十进制   decimal  
- 十六进制  hex     0x开头

## 说明
    十进制的数是int型，其他的都是str类型
    需要转的数本身是10进制，不需要加base参数

## 转换成10进制
    int('', base=10)
```
2进制转化成10进制
>>> int("0b101010", base=2)
Out[179]: 42

>>> int("101010", base=2)
Out[180]: 42

>>> int(0b101010)
Out[181]: 42
```

## 10进制转换成2进制
```
>>> bin(10)
>>> '0b1010'
```

## 10进制转换成16进制
```
>>> hex(42)  
>>> '0x2a'

>>> hex(12648430)
>>> '0xc0ffee'
```

## 转换成八进制
```
>>> int(0b1010)
Out[183]: 10

>>> oct(10)
Out[184]: '0o12'

>>> oct(0b1010)
Out[185]: '0o12'  
```
