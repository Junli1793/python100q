#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。

"""

print()
print("==============Answer 1==============")

a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100, 0]
print('原始列表:')
for i in range(len(a)):
    print(a[i])
number = int(input("\n插入一个数字:\n"))
end = a[9]
if number > end:
    a[10] = number
else:
    for i in range(10):
        if a[i] > number:
            temp = a[i]
            a[i] = number
            for j in range(i + 1, 11):
                temp1 = a[j]
                a[j] = temp
                temp = temp1
            break

print('排序后列表:')
for i in range(11):
    print(a[i])

print()
print("==============Answer 2==============")

b = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100, 0]

number = int(input("\n插入一个数字:\n"))
end = b[9]

if number > end:
    b[10] = number
else:
    for i in range(0, 10):
        if b[i] > number:
            temp1 = b[i]
            b[i] = number
            for j in range(10, i, -1):
                b[j] = b[j-1]
            b[i+1] = temp1
            break

print('排序后列表:')
for i in range(11):
    print(b[i])


