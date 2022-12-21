#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
reduce() 函数会对参数序列中元素进行累加。

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
    用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
    得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

注意：Python3.x reduce() 已经被移到 functools 模块里，如果我们要使用，需要引入 functools 模块来调用 reduce() 函数：
    from functools import reduce

reduce() 函数语法：
    reduce(function, iterable[, initializer])

    function -- 函数，有两个参数
    iterable -- 可迭代对象
    initializer -- 可选，初始参数

"""

from functools import reduce


print()
print("==============Example 1==============")

def add(x, y):  # 两数相加
    return x + y


sum1 = reduce(add, [1, 2, 3, 4, 5])  # 计算列表和：1+2+3+4+5
sum2 = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
print(sum1)
print(sum2)


print()
print("==============Example 2==============")


def add(x, y):
    return x + y


print(reduce(add, range(1, 101)))
print(reduce(lambda x, y: x + y, range(1, 101)))

print()
print("==============Example 3==============")

sentences = ['The Deep Learning textbook is a resource intended to help students and practitioners enter the field of '
             'machine learning in general and deep learning in particular. ']
word_count = reduce(lambda a, x: a + x.count("learning"), sentences, 0)
                                # a = 0
                                # x = sentences
print(word_count)

print()
print("==============Example 4==============")

str1 = "hello"
print(reduce(lambda x, y: y + x, str1))
# 输出 olleh
