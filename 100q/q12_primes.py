#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：判断101-200之间有多少个素数，并输出所有素数。

程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。

"""

print()
print("==============Answer 1==============")

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


def check_prime(number):
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0:
            return False
    return True


class Primes:

    def __init__(self, max):
        self.max = max
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number >= self.max:
            raise StopIteration
        elif check_prime(self.number):
            return self.number
        else:
            return self.__next__()


def Primes_f(max):
    number = 1
    while number < max:
        number += 1
        if check_prime(number):
            yield number


print()
print("==============Answer 2==============")


primes = Primes(100)
print(primes)
for x in primes:
    print(x)


print()
print("==============Answer 3==============")


primes = Primes_f(100)
print(primes)
for x in primes:
    print(x)


print()
print("==============Answer 4==============")

primes = (i for i in range(2, 100) if check_prime(i))
print(primes)
for x in primes:
    print(x)

