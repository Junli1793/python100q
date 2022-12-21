#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

"""

print()
print("==============Answer 1==============")

a = int(input("请输入一个数字:\n"))
x = str(a)
flag = True

for i in range(len(x) // 2):
    if x[i] != x[-i - 1]:
        flag = False
        break
if flag:
    print("%d 是一个回文数!" % a)
else:
    print("%d 不是一个回文数!" % a)

print()
print("==============Answer 2==============")

a = input("输入一串数字: ")
b = a[::-1]
print(b)
if a == b:
    print("%s 是回文" % a)
else:
    print("%s 不是回文" % a)

