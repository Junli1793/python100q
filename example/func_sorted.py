#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
Python3 sorted() 函数
https://www.runoob.com/python3/python3-func-sorted.html

sorted() 函数对所有可迭代的对象进行排序操作。
    sort 与 sorted 区别：
    1, sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
    2, list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

sorted 语法：
    sorted(iterable, cmp=None, key=None, reverse=False)

参数说明：
    1, iterable -- 可迭代对象。
    2, cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
    3, key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    4, reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

返回值:
    返回重新排序的列表。

"""

print()
print("==============Example 1==============")

a = [5, 7, 6, 3, 4, 1, 2]
b = sorted(a)

print("原列表不变")
print(a)
print("返回列表")
print(b)

print()
print("==============Example 2==============")

l2 = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
print("利用key")
c = sorted(l2, key=lambda x: x[1])
print(c)

print()
print("==============Example 3==============")

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

print("按年龄排序")
a = sorted(students, key=lambda s: s[2])
print(a)

print("按年龄降序")
b = sorted(students, key=lambda s: s[2], reverse=True)
print(b)

print("先分数排序，再按年龄排序")
b = sorted(students, key=lambda s: (s[1], s[2]))
print(b)


print()
print("==============Example 4==============")

print("原列表：")
a = [[1, 3], [3, 2], [2, 4], [1, 2], [1, 5], [2, 5]]
print(a)

print("先按第一个元素升序排序，第一个元素相同按第二个元素升序排序")
a.sort()
print(a)

print("先按第一个元素升序排序，第一个元素相同则保持原来的顺序")
a = [[1, 3], [3, 2], [2, 4], [1, 2], [1, 5], [2, 5]]
a.sort(key=lambda x: x[0])
print(a)

print("先按第二个元素升序排序，第二个元素相同则保持原来的顺序")
a = [[1, 3], [3, 2], [2, 4], [1, 2], [1, 5], [2, 5]]
a.sort(key=lambda x: x[1])
print(a)

print("先按第二个元素升序排序，第二个元素相同按第一个元素降序排序")
a.sort(key=lambda x: (x[1], -x[0]))
print(a)

