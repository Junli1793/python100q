#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import time

myD = {1: 'a', 2: 'b'}
for key, value in myD.items():
    print(key, value)
    time.sleep(1)  # 暂停 1 秒

myDic = {1: 'aaa', 3: 'ccc'}
for k, v in dict.items(myDic):
    print(k, v)
    time.sleep(1)

"""
merge 2 dicts
"""
print("update")
myD.update(myDic)
for k3, v3 in myD.items():
    print(k3, v3)
    time.sleep(1)

print("高级方法")

### In Python 3.9.0 or greater
# z = myD | myDic
# print(z)

"""
What does ** (double star) and * (star) do for parameters？
They allow for functions to be defined to accept and for users to pass any number of arguments, positional (*) and keyword (**).
Defining Functions
*args allows for any number of optional positional arguments (parameters), which will be assigned to a tuple named args. 
**kwargs allows for any number of optional keyword arguments (parameters), which will be in a dict named kwargs.
"""
dic4 = {**myD, **myDic}
for k4, v4 in dict.items(dic4):
    print(k4, v4)
    time.sleep(1)
"""

You can also make a function to merge an arbitrary number of dictionaries, from zero to a very large number:
"""
def merge_dicts(*dict_args):
    """
    Given any number of dictionaries, shallow copy and merge into a new dict,
    precedence goes to key-value pairs in latter dictionaries.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result
