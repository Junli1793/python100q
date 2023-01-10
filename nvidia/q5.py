#!/usr/bin/python3
# -*- coding: UTF-8 -*-

lsn = []
for n in range(100, 1000):
    i = n // 100
    j = n // 10 % 10
    k = n % 10
    if i ** 3 + j ** 3 + k ** 3 == n:
        lsn.append(n)

print(lsn)
