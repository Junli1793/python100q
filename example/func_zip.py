#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。

我们可以使用 list() 转换来输出列表。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

"""

print()
print("==============Example 1==============")

a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
zipped = zip(a, b)  # 返回一个对象

print(list(zipped))  # list() 转换为列表

print(list(zip(a, c)))  # 元素个数与最短的列表一致

print()
print("==============Example 2==============")

a1, a2 = zip(*zip(a, b))  # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
print(a1)
print(a2)
print(list(a1))
print(list(a2))

print()
print("==============Example 3==============")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

zipped = zip(list1, list2, list3)
print("First time:", list(zipped))  # Output: [(1, 4, 7), (2, 5, 8), (3, 9, 9)]
print("Second time:", list(zipped))  # []
# the returned object from zip is an iterator,
# so if you want to use it multiple times you have to convert it to a list or another iterable.

print("call zip again:")
zipped = zip(list1, list2, list3)
l1, l2, l3 = zip(*zipped)
print(list(l1))
print(list(l2))
print(list(l3))

print()
print("==============Example 4==============")

zipped = zip([list1, list2, list3])
print(list(zipped))  # Output: [(1, 4, 7), (2, 5, 8), (3, 9, 9)]

zipped = zip(list1)
print(list(zipped))

