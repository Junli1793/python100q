#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
打印出如下图案（菱形）

"""

print()
print("==============Answer 1==============")

for i in range(0, 4):
    c_a = 1 + i * 2
    c_s = 3 - i
    print(' ' * c_s, "*" * c_a)
for i in range(2, -1, -1):
    c_a = 1 + i * 2
    c_s = 3 - i
    print(' ' * c_s, "*" * c_a)

for i in range(4):
    print((3-i)*' '+(2*i+1)*'*')
for i in range(3):
    print((i+1)*' '+(5-2*i)*'*')

print()
print("==============Answer 2==============")

from sys import stdout

for i in range(4):
    for j in range(2 - i + 1):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print('')

for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print('')

print()
print("==============Answer 3==============")

# n = int(input('enter an odd number:'))
n = 7
for i in range(1, n + 1, 2):
    k = (n - i) // 2
    print(' ' * k, '*' * i)

for j in range(n - 2, 0, -2):
    o = (n - j) // 2
    print(' ' * o, '*' * j)

