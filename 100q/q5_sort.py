#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
https://www.runoob.com/python/python-exercise-example5.html

题目：输入三个整数x,y,z，请把这三个数由小到大输出。

程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。

"""

l = [2, 1, 9, 4, 3, 5, 7, 8, 6]
# for i in range(3):
#     x = int(input("integer:\n"))
#     l.append(x)

l.sort()
print(l)

l.sort(reverse=True)
print(l)


# 2022-12-07
n = len(l)
for i in range(n):
    for j in range(i, n):
        if l[i] > l[j]:
            # temp = l[i]
            # l[i] = l[j]
            # l[j] = temp
            l[i], l[j] = l[j], l[i]

print(l)

