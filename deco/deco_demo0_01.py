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


def add_params(a, b):
    return a + b


def mult_params(func, a, b, c):
    return func(a, b) * c


a, b, c = 1, 2, 3

# add_params(a,b)= 1 + 2 = 3
r1 = add_params(a, b)

# mult_params(func,a,b,c) = (1+2)*3 = 3*3 = 9
r2 = mult_params(add_params, a, b, c)

print(r1)
print(r2)

print()
print("==============Example 2==============")


def mult_dict(func, c, **params):
    return func(**params) * c


r3 = mult_dict(add_params, c, b=2, a=1)
print(r3)
