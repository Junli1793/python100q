#!/usr/bin/python3
# -*- coding: UTF-8 -*-
l = []
for i in range(3):
    x = int(input("integer:\n"))
    l.append(x)

l.sort()
print(l)
l.sort(reverse=True)
print(l)


# 2022-12-07
n = len(l)
for i in range(n):
    for j in range(i, n):
        if l[i] > l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

print(l)

