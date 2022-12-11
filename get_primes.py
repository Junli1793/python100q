#!/usr/bin/python
# -*- coding: UTF-8 -*-


def check_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
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
                    
# primes = Primes(1000000000)
# print(primes)
# for x in primes:
#     print(x)

# primes = Primes_f(1000000000)
# print(primes)
# for x in primes:
#     print(x)


primes = (i for i in range(2, 1000000) if check_prime(i))
print(primes)
for x in primes:
    print(x)

