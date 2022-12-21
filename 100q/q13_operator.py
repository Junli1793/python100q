#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
    例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
"""

print()
print("==============Answer 1==============")

lsn = []
for n in range(100, 1000):
    i = n // 100
    j = n // 10 % 10
    k = n % 10
    if i ** 3 + j ** 3 + k ** 3 == n:
        lsn.append(n)

print(lsn)

print()
print("==============Answer 2==============")

for x in range(1, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            s1 = x * 100 + y * 10 + z
            s2 = pow(x, 3) + pow(y, 3) + pow(z, 3)
            if s1 == s2:
                print("水仙花数有：%7ld" % (s1))

print()
print("==============Answer 3==============")

for i in range(100, 1000):
    s = str(i)
    if int(s[0]) ** 3 + int(s[1]) ** 3 + int(s[2]) ** 3 == i:
        print(i)

print()
print("==============Answer 4==============")


# 生成器函数ppdi,可生成十进制自然数中的所有水仙花数，共有88个
def ppdi():
    n = 3
    while 1:
        # 生成器推导式
        l = (i for i in range(10 ** (n - 1), 10 ** n) if sum([int(str(i)[j]) ** n for j in range(n)]) == i)
        yield l
        n += 1


def f(max):
    for i in ppdi():
        for j in i:
            if j < 10 ** max:
                print(j)
            else:
                break
        if j > 10 ** max:
            break


# 为环保起见，建议7位以内即可
f(3)
