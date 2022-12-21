#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

"""

print()
print("==============Answer 1==============")

height = 100
h_list = [100]
for i in range(10):
    h_list.append(h_list[-1] / 2)

print(h_list)
print(sum(h_list[1:10]) * 2 + 100)
print(h_list[10])

print()
print("==============Answer 2==============")

tour = []
height = []

hei = 100.0  # 起始高度
tim = 10  # 次数

for i in range(1, tim + 1):
    # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2 * hei)
    hei /= 2
    height.append(hei)

print('总高度：tour = {0}'.format(sum(tour)))
print('第10次反弹高度：height = {0}'.format(height[-1]))

print()
print("==============Answer 3==============")

sum1 = 0
total = 0
for i in range(1, 10):
    sum1 = (100 * 2) / (2 ** i)
    total += sum1
result = 100 + total
tenth = 100 / (2 ** 10)
print('第10次反弹高度: {}'.format(tenth))
print('第10次反弹后，一共经历的距离: {}'.format(result))

print()
print("==============Answer 4==============")


# h 为初始高度，k 为每次弹起的高度比例，如本题弹起一半即为 0.5，n 为反弹次数
def Sumh(h, k, n):
    L = []
    for i in range(1, n + 1):
        h *= k
        totalh = h * 3
        L.append(totalh)
    print(h)
    print(sum(L) - h)  # 第 10 次落地高度，要去除最后一次反弹


Sumh(100, 0.5, 10)

print()
print("==============Answer 5==============")

a = 100.00
b = 0.0
print(a / (2 ** 10))
for i in range(0, 10):
    b, a = b + 2 * a, a / 2
print(b - 100)

print()
print("==============Answer 6==============")

import math

# 设落地n次
n = int(input("请输入反弹次数："))
height = 100
print("第{}次落地共: {:<8}米".format(n, height * (3 - math.pow(2, -(n - 2)))))
print("第{}次反弹: {:<8}米".format(n, height * math.pow(2, -n)))
