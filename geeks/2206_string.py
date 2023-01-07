#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。

Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。

"""

print()
print("==============Example 1: Python字符串运算符==============")

a = "Hello "
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])

print("b[:] 输出结果：", b[:])
print("b[1:4] 输出结果：", b[1:4])
print("b[-4] 输出结果：", b[-4])
print("b[-4:-1] 输出结果：", b[-4:-1])
print("b[-1] 输出结果：", b[-1])

print("b[::2] 输出结果：", b[::2])
print("b[::-1] 输出结果：", b[::-1])

if "H" in a:
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if "M" not in a:
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print('\n')
print(r'\n')
print('\n')
print(R'\n')

print()
print("==============Example 2: Python字符串格式化==============")

print("%s 格式化字符串, %d 格式化整数")
print("我叫 %s 今年 %d 岁!" % ('小明', 10))
num = 18.7254
print("%f 格式化浮点数字，可指定小数点后的精度")
print("the price is %.2f" % num)
print()

b = '1'
bs_len = len(b)
print('int(b_b, 2)，二进制转化成十进制')
while bs_len < 9:
    b_b = b.ljust(8, '0')
    d = int(b_b, 2)
    print('二进制 %s 相当于十进制 %s' % (b_b, d))
    b = b + "1"
    bs_len = len(b)

