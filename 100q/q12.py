#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
"""

leap = 1
from math import sqrt
from sys import stdout


def get_prime_number(num1, num2):

    ln = []
    for n in range(num1, num2):
        h = 0
        for i in range(2, int(sqrt(n+1)) + 1):
            if n % i == 0:
                h = 1
                break

        if h == 0:
            ln.append(n)

    return ln, len(ln)


primes, n = get_prime_number(2, 100)

print(primes)
print(n)


print(get_prime_number(101, 201))
