#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：输出一个随机数。

"""


print()
print("==============Answer 1==============")

import random

#生成 10 到 20 之间的随机数
print(int(random.random()*10) + 10)

print(random.uniform(10, 20))

print(random.randint(10, 20))

print(random.choice([x for x in range(1, 100)]))    #输出1-99间的随机数

