#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。
"""


print()
print("==============Answer 1==============")

first_l = input("input first letter")

if first_l.upper() == "M":
    print("Monday")
elif first_l.upper() == "T":
    second_l = input("input second letter")
    if second_l.upper() == "U":
        print("Tuesday")
    elif second_l.upper() == "H":
        print("Thursday")
elif first_l.upper() == "W":
    print("Wednesday")
elif first_l.upper() == "F":
    print("Friday")
elif first_l.upper() == "S":
    second_l = input("input second letter")
    if second_l.upper() == "U":
        print("Sunday")
    elif second_l.upper() == "A":
        print("Saturday")
else:
    print('data error')