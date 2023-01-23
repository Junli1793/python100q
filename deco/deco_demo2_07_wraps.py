#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
这并不是我们想要的！Ouput输出应该是"a_function_requiring_decoration"。
这里的函数被warpTheFunction替代了。它重写了我们函数的名字和注释文档(docstring)。
幸运的是Python提供给我们一个简单的函数来解决这个问题，那就是functools.wraps。
我们修改上一个例子来使用functools.wraps：
'''

from functools import wraps

print()
print("==============Example 1==============")

def a_new_decorator(a_func):

    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

 
@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")


a_function_requiring_decoration()
print(a_function_requiring_decoration.__name__)  # Output: a_function_requiring_decoration
print(type(a_function_requiring_decoration))

print()
print("==============Example 2==============")

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
