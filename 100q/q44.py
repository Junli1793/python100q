#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：

程序分析：创建一个新的 3 行 3 列的矩阵，使用 for 迭代并取出 X 和 Y 矩阵中对应位置的值，相加后放到新矩阵的对应位置中。
"""

print()
print("==============Answer 1==============")

X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(3):
    for j in range(3):
        result[i][j] = X[i][j] + Y[i][j]

print(result)

print()
print("==============Answer 2==============")

x = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

z = []
for i in range(3):
    z.append([])

print(z)
for i in range(3):
    # print(z[i])
    for j in range(3):
        z[i].append(x[i][j] + y[i][j])
print(z)

print()
print("==============Answer 3==============")

import numpy as np

x = np.array([[12, 7, 3],
              [4, 5, 6],
              [7, 8, 9]])
y = np.array([[5, 8, 1],
              [6, 7, 3],
              [4, 5, 9]])

z = x + y
print(z)
