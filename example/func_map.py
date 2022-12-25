#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

map() 函数语法：
map(function, iterable, ...)

"""

print()
print("==============Example 1==============")

def square(x):  # 计算平方数
    return x ** 2

map(square, [1, 2, 3, 4, 5])  # 计算列表各个元素的平方

l1 = list(map(square, [1, 2, 3, 4, 5]))  # 使用 list() 转换为列表
l2 = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))  # 使用 lambda 匿名函数
# [1, 4, 9, 16, 25]

print(l1)
print(l2)

print()
print("==============Example 2==============")

name_list = {'tony', 'cHarLIE', 'rachAEl'}


def format_name(s):
    ss = s[0:1].upper() + s[1:].lower()
    return ss


print(list(map(format_name, name_list)))

type(name_list)

print()
print("==============Example 3==============")

res1 = map(lambda n: n > 5, range(10))
lt1 = list(res1)
print(lt1)

res2 = filter(lambda n: n > 5, range(10))
lt2 = list(res2)
print(lt2)

print()
print("==============Example 4==============")

listx = [1, 2, 3, 4, 5, 6, 7]  # 7 个元素
listy = [2, 3, 4, 5, 6, 7]  # 6 个元素
listz = [100, 100, 100, 100]  # 4 个元素
list_result = map(lambda x, y, z: x ** 2 + y + z, listx, listy, listz)
print(list(list_result))
# [103, 107, 113, 121]
