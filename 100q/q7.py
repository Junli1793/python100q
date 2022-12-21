#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：将一个列表的数据复制到另一个列表中。
程序分析：使用列表[:]。

"""
import copy

print()
print("==============Answer 1==============")

a = [1, 2, 3]
b = a[:]
print(b)

print()
print("==============Answer 2==============")

a = [1, 2, 3]
b = []

for i in range(len(a)):
    b.append(a[i])

print(b)

print()
print("==============Answer 3==============")

b = a.copy()
print(b)

a.append([1, 2, 3, 4, 5])
print(a)
print("==============Answer 3: copy==============")
b = a.copy()
print(b)
print("==============Answer 3: copy.deepcopy==============")
copy.deepcopy(b)
print(b)

print()
print("==============Answer 4==============")

b = [i for i in a]
print(b)

print()
print("==============Answer 5==============")

print("==============Answer 5: assign==============")
b = a
print(b)
a[0] = 11
print(a)
print(b)
print("==============Answer 5: a * 1==============")
b = a * 1
print(b)
a[0] = 111
print(a)
print(b)

