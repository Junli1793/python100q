#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0开头。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


def addTwoNumbers(l1, l2):
    len1 = len(l1)
    len2 = len(l2)
    # len3 = len2 if len1 >= len2 else len1

    if len1 >= len2:
        l1.append(0)
        len3 = len1 + 1

        l2.extend([0 for i in range(len1 - len2 + 1)])
        # print(l2)

    l3 = []
    large_than_ten = 0
    # print(len3)
    for i in range(len3):

        if large_than_ten == 0:
            temp = l1[i] + l2[i]
        else:
            temp = l1[i] + l2[i] + 1

        if temp > 10:
            l3.append(temp - 10)
            large_than_ten = 1
        elif temp == 10:
            l3.append(0)
            large_than_ten = 1
        else:
            l3.append(temp)
            large_than_ten = 0
    # print(l3)
    if l3[-1] == 0:
        l3.pop()

    return l3


print(addTwoNumbers([0], [0]))
print(addTwoNumbers([2, 4, 3], [5, 6, 4]))
# addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])
print(addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
