#!/usr/bin/python3
# -*- coding: UTF-8 -*-


print()
print("==============Answer 1==============")

x = 10
# x = int(input("Please input a number:"))

def fib1(n):
    if (n == 1) or (n == 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)

l = []
for i in range(1, x + 1):
    l.append(fib1(i))
print(l)

print()
print("==============Answer 2==============")

def fib2(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

# 输出前 10 个斐波那契数列
print(fib2(x))

print()
print("==============Answer 3==============")

def fib3(n):
    a, b = 1, 1
    for i in range(n - 2):
        a, b = b, a + b
        print(f"a: {a}")
        print(f"b: {b}")
    return b

print(fib3(x))

