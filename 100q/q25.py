#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：求1+2!+3!+...+20!的和。

程序分析：此程序只是把累加变成了累乘。

"""

print()
print("==============Answer 1==============")

sm = 0
for i in range(1, 21):
    nn = 1
    for j in range(1, i + 1):
        nn *= j
    sm += nn

print(sm)

print()
print("==============Answer 2==============")

n = 0
s = 0
t = 1
for n in range(1, 21):
    t *= n
    s += t
print('1! + 2! + 3! + ... + 20! = %d' % s)

print()
print("==============Answer 3==============")

s = 0
ll = range(1, 21)
def op(x):
    r = 1
    for i in range(1, x + 1):
        r *= i
    return r

s = sum(map(op, ll))
print('1! + 2! + 3! + ... + 20! = %d' % s)

print()
print("==============Answer 4==============")

s=0
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

for n in  range(1,21):
    a = fact(n)
    s += a
print(s)

print()
print("==============Answer 5==============")

s = 1
t = []
for i in range(1,21):
    s *= i
    t.append(s)
print(sum(t))

