#!/usr/bin/python
# -*- coding: UTF-8 -*-
l = []
for i in range(3):
    x = int(input("integer:\n"))
    l.append(x)

# l.sort()
# print(l)


# 2022-12-07
n = len(l)
for i in range(0, n):
    for j in range(i, n):
        if l[i] > l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

print(l)

# n = len(l)
# for i in range(0, n):
#     for j in range(i, n):
#         if l[i] > l[j] :
#             tmp = l[i]
#             l[i] = l[j]
#             l[j] = tmp
# print(l)
