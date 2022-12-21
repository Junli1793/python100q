#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

程序分析：关键是计算出每一项的值。

"""

from functools import reduce

print()
print("==============Answer 1==============")

nn = 0
num_list = []
sumn = 0

nn = int(input('数字个数nn '))
num = input('数字num ')

for i in range(1, nn + 1):
    temp = int(num * i)
    num_list.append(temp)
    sumn += temp
    print(temp)

print(num_list)
print(sumn)

print()
print("==============Answer 2==============")

Tn = 0
Sn = []
n = int(input('n = '))
a = int(input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)

print(Sn)
print(sum(Sn))
print()
Sn = reduce(lambda x, y: x + y, Sn)
print("计算和为：", Sn)

print()
print("==============Answer 3==============")

n = int(input('n = '))
a = int(input('a = '))
sum = 0
total = 0
for i in range(n):
    sum += (10 ** i)
    total += sum * a
print(total)

print()
print("==============Answer 4==============")


def f(n, a):
    if (n == 1):
        return a
    else:
        r = f(n - 1, a) * 10 + a
        return r


n = int(input("n=\n"))
a = int(input("a=\n"))
print("")
sum1 = 0
for i in range(1, n + 1):
    print(f(i, a))
    sum1 = sum1 + f(i, a)

print("sum=", sum1)

print()
print("==============Answer 5==============")
n = input('请输入计算数:')
m = eval(input('请输入层数:'))
s = 0
for i in range(1, m + 1):
    a = n * i
    s += eval(a)
print('{}'.format(s))
