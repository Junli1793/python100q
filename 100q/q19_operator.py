#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
程序分析：请参照程序Python 练习实例14。

"""

print()
print("==============Answer 1==============")
# n = int(input("Please input a number:"))
n = 6
for n in range(2, 1001):
    list_factor = [1]
    # for i in range(2, int(n / 2) + 1):
    for i in range(2, n // 2 + 1):  # // 取整除 - 向下取接近商的整数
        if n % i == 0:              # % 取模 - 返回除法的余数
            list_factor.append(i)

    # sumf = 0
    # for i in list_factor:
    #     sumf += i

    # if sumf == n:
    if n == sum(list_factor):
        print(n)
        print(list_factor)

print()
print("==============Answer 2==============")

from sys import stdout

for j in range(2, 1001):
    k = []
    n = -1
    s = j
    for i in range(1, j):
        if j % i == 0:
            n += 1
            s -= i
            k.append(i)

    if s == 0:
        print(j)
        for i in range(n):
            stdout.write(str(k[i]))
            stdout.write(' ')
        print(k[n])
