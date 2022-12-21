#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：利用递归方法求5!。

程序分析：递归公式：fn=fn_1*4!

"""

print()
print("==============Answer 1==============")


def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


print(factorial(5))
