#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：输出 9*9 乘法口诀表。
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。

"""

print()
print("==============Answer 1==============")

for i in range(1, 10):
    print()
    for j in range(1, i + 1):
        print("%dx%d=%d " % (i, j, i * j), end='')

print()
print("==============Answer 2==============")

i = 0
j = 0
while i < 9:
    i += 1
    while j < 9:
        j += 1
        print(j, "x", i, "=", i * j, "\t", end="")
        if i == j:
            j = 0
            print("")
            break

print()
print("==============Answer 3==============")

for i in range(1, 10):
    l = []
    for j in range(1, i + 1):
        l.append(str(j) + "X" + str(i) + "=" + str(i * j))
    print(" ".join(l))
