#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# a = [1, 2, 3]
# b = a[:]
# print b

a = [1, 2, 3]
b = []

### Method: 1
for i in range(len(a)):
    b.append(a[i])
    
print(b)

### Method: 2
c = a[:]
print(c)
