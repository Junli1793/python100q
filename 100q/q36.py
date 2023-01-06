#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：求100之内的素数。

"""

print()
print("==============Answer 1==============")

for i in range(2, 100):
    prime = True
    for j in range(2, int(i / 2) + 1):
        if i % j == 0:
            prime = False
            break
    if prime: print(i)

print()
print("==============Answer 2==============")

lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))

for num in range(lower, upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

