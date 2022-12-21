#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

程序分析：程序分析：(a>b) ? a:b 这是条件运算符的基本例子。

"""

print()
print("==============Answer 1==============")


score = int(input('输入分数:\n'))
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'

print('%d 属于 %s' % (score, grade))

print()
print("==============Answer 2==============")


def k(x):
    if x in range(60):
        print('C')
    elif x in range(60, 90):
        print('B')
    else:
        print('A')


# score = int(input('输入分数:\n'))
k(score)

print()
print("==============Answer 3==============")

# score = int(input('输入分数：'))
print('A' if score > 89 else ('B' if score > 59 else 'C'))

print()
print("==============Answer 4==============")

# score = int(input('输入分数:\n'))
print(['C', 'C', 'B', 'A'][score // 30])
