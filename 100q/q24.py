#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

程序分析：请抓住分子与分母的变化规律。

"""
from functools import reduce

print()
print("==============Answer 1==============")


def fib1(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib2(n - 1) + fib2(n - 2)


list_1 = [fib1(i) for i in range(1, 21)]
list_2 = [fib2(i) for i in range(1, 21)]

print(list_1)
print(list_2)

list_3 = [list_1[i] / list_2[i] for i in range(0, 20)]
print(sum(list_3))

print()
print("==============Answer 2==============")

a = 2.0
b = 1.0
s = 0
for n in range(1, 21):
    s += a / b
    t = a
    a = a + b
    b = t
print(s)

print()
print("==============Answer 3==============")

a = 2.0
b = 1.0
s = 0.0
for n in range(1, 21):
    s += a / b
    b, a = a, a + b

print(s)

print()
print("==============Answer 4==============")

a = 2.0
b = 1.0
ll = [a / b]
for n in range(1, 20):
    b, a = a, a + b
    ll.append(a / b)
print(reduce(lambda x, y: x + y, ll))

