#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""

"""


print()
print("==============Example 1: 1==============")

import re
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Modify the behavior of the function
        print('Before calling the decorated function')
        result = func(*args, **kwargs)
        print('After calling the decorated function')
        return result
    return wrapper

@my_decorator
def my_function(a, b):
    print(a + b)

my_function(1, 2)
print(my_function.__name__)
print(type(my_function))
