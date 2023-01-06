#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：对10个数进行排序。

程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。

"""

print()
print("==============Answer 1: 冒泡法==============")

a = [9, 0, 4, 8, 5, 2, 7, 6, 3, 1]
n = len(a)
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)

print()
print("==============Answer 2: list1.sort()==============")

a = [9, 0, 4, 8, 5, 2, 7, 6, 3, 1]
a.sort()
print(a)

print()
print("==============Answer 3: sorted(list1)==============")

a = [9, 0, 4, 8, 5, 2, 7, 6, 3, 1]
print(sorted(a))
