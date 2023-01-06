#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
Python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
    1, lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
    2, lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。

A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

lambda 函数的语法只包含一个语句，如下：
    lambda [arg1 [,arg2,.....argn]]:expression

"""

print(">>>lambda: anonymous function")
print()
print("==============Example 1==============")

x = lambda a, b: a * b
print(x(5, 6))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

# 可写函数说明
sum1 = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum1(10, 20))
print("相加后的值为 : ", sum1(20, 20))

print()
print("==============Example 2==============")

print(">>> The power of lambda is better shown when you use them as an anonymous function inside another function.")

def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
"""
def mydoubler(a):
    return a*2
"""

mytripler = myfunc(3)
"""
def mytripler(a):
    return a*3
"""

print(mydoubler(11))
print(mytripler(11))

