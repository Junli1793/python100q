#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
该接收两个参数，第一个为函数，第二个为序列，
序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

语法:
    filter(function, iterable)

    function -- 判断函数。   # function must return True or False
    iterable -- 可迭代对象。

"""


print()
print("==============Example 1==============")

def is_odd(n):
    return n % 2 == 1

newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(newlist)
print(list(newlist))

print()
print("==============Example 2==============")

import math
def is_sqr(x):
    return math.sqrt(x) % 1 == 0

newlist = filter(is_sqr, range(1, 101))
print(newlist)
print(list(newlist))


print()
print("==============Example 3==============")

input_list = ['Delhi', 'Mumbai', 'Noida', 'Gurugram']
to_match ='Gurugram'

matched_list = list(filter(lambda item: True if item == to_match else False, input_list))
print(matched_list)

