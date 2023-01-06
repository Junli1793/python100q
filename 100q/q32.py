#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：按相反的顺序输出列表的值。
"""


print()
print("==============Answer 1==============")
l1 = [2, 3, 4, 1]

for i in range(len(l1)-1, -1, -1):
    print(l1[i])

print()
print("==============Answer 2==============")

a = ['one', 'two', 'three']
print(a[::-1])
print(a[::])
print(a[2:2])   #[]
print(a[2:3])
for i in a[::-1]:
    print(i)
