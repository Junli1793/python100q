#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Python中将函数作为参数传递给函数

Everything is object in Python.
Python中一切皆对象(object).

既然一切皆对象，那么一切都可以作为参数传递

"""

print()
print("==============Example 1==============")


def add_params(a1, b1):
    return a1 + b1


def mult_params(func, a1, b1, c1):
    return func(a1, b1) * c1


a, b, c = 1, 2, 3

# add_params(a,b)= 1 + 2 = 3
r1 = add_params(a, b)

# mult_params(func,a,b,c) = (1+2)*3 = 3*3 = 9
r2 = mult_params(add_params, a, b, c)

print(r1)
print(r2)

print()
print("==============Example 2==============")


def mult_dict(func, c2, **params):
    return func(**params) * c2


r3 = mult_dict(add_params, c, b=2, a=1)
print(r3)

print()
print("==============Example 3: closure==============")


def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Modify the behavior of the decorated function
        print('Before calling the decorated function')
        result = func(*args, **kwargs)
        print('After calling the decorated function')
        return result
    return wrapper


def my_function(a3, b3):
    print(a3 + b3)


my_function = my_decorator(my_function)

my_function(1, 1)
my_function(2, 3)
my_function(5, 8)


print()
print("==============Example 4: lambda==============")


def myfunc(n):
    return lambda a4: a4 * n


mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
