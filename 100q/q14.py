#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
    (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
    (2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
    (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。

"""

print()
print("==============Answer 1==============")


def reduceNum(n):
    print('{} = '.format(n), end=" ")
    if not isinstance(n, int) or n <= 0:
        print('请输入一个正确的数字 !')
        exit(0)
    elif n in [1]:
        print('{}'.format(n))
    while n not in [1]:  # 循环保证递归
        for index in range(2, n + 1):
            if n % index == 0:
                n //= index  # n 等于 n//index
                if n == 1:
                    print(index)
                else:  # index 一定是素数
                    print('{} *'.format(index), end=" ")
                break


reduceNum(90)
reduceNum(100)

print()
print("==============Answer 2==============")


def prime(n):
    l = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = int(n / i)
                l.append(i)
                break
    return l


s = input("输入一个正整数:")
if s.isdigit() and int(s) > 0:
    print(s, "=", "*".join([str(x) for x in prime(int(s))]))
else:
    print("请输入正确的正整数")

print()
print("==============Answer 3==============")

inn = int(input("请输入要分解的正整数："))

temp = []
while inn != 1:
    for i in range(2, inn + 1):
        if inn % i == 0:
            temp.append(i)
            inn = inn // i
            break
print(temp)

print()
print("==============Answer 4==============")

n = int(input("Please input a number:"))
n1 = n
l = []
while n > 1:
    for i in range(2, n + 1):
        if n % i == 0:
            n = n // i
            l.append(str(i))
            break

print('%d=' % n1 + '*'.join(l))
