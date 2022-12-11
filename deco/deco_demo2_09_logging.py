#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
日志是装饰器运用的另一个亮点.
'''

from functools import wraps

 
def logit(func):

    @wraps(func)
    def with_logging_wrapper(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging_wrapper

 
@logit
def addition_func(x):
   """Do some math."""
   return x + x
 
 
print("#################1")
result = addition_func(4)
# Output: addition_func was called
print(result)

print("#################2")
print(addition_func(8))

print("#################3")
print(addition_func(8) + addition_func(8))

print("#################4")
print(addition_func(addition_func(8)))
