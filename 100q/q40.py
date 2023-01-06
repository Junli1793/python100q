#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：将一个数组逆序输出。

程序分析：用第一个与最后一个交换。
"""
from functools import reduce

print()
print("==============Answer 1==============")

a = [9, 6, 5, 4, 1]
print(a[::-1])

print()
print("==============Answer 2==============")

a = [9, 6, 5, 4, 1]
a.reverse()
print(a)

