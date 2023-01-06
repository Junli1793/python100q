#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：统计 1 到 100 之和。
"""
from functools import reduce

print()
print("==============Answer 1==============")

sums = 0
for i in range(1, 101):
    sums += i

print(sums)

print()
print("==============Answer 2==============")

print(sum(range(1, 101)))

print()
print("==============Answer 3==============")

print(reduce(lambda x, y: x + y, range(1, 101)))


