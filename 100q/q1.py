#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
https://www.runoob.com/python/python-exercise-example1.html

题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

"""

print()
print("==============Answer 1==============")

d = []
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):
                d.append([i, j, k])

for i in d:
    print(i)
print("总数量：", len(d))

print()
print("==============Answer 2==============")

n = 0
for i in range(1, 5):
    for j in range(1, 5):
        if j == i:
            continue
        for k in range(1, 5):
            if k == i or k == j:
                continue
            print(i, j, k)
            n += 1

print("总数量：", n)

print()
print("==============Answer 3==============")

list3 = [1, 2, 3, 4]
n = 0
for i in list3:
    list1 = list3.copy()
    list1.remove(i)
    for j in list1:
        list2 = list1.copy()
        list2.remove(j)
        for k in list2:
            print(i, j, k)
            n += 1

print("总数量：", n)
