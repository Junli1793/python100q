#!/usr/bin/python
# -*- coding: UTF-8 -*-
def fib1(n):
    if (n == 1) or (n == 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def fib3(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


l = []
x = int(input("number:"))
# input 36
for i in range(1, x + 1):
    l.append(fib1(i))
print(l)

# 输出前 10 个斐波那契数列
print(fib2(x))

print(fib3(x))
