#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。

isinstance() 与 type() 区别：
    type() 不会认为子类是一种父类类型，不考虑继承关系。
    isinstance() 会认为子类是一种父类类型，考虑继承关系。

如果要判断两个类型是否相同推荐使用 isinstance()。

语法:
isinstance(object, classinfo)
    object -- 实例对象。
    classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。

返回值:
如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False。

"""

print()
print("==============Example 1==============")

arg = 123
print(isinstance(arg, int))
print(isinstance(arg, str))
print(isinstance(arg, (str, int, list)))

print()
print("==============Example 2==============")

def normalize_dict(input_dict):
    '''
    Expanding nested dicts into normalized dict using recursion
    '''
    result = {}
    for key, val in input_dict.items():
        if isinstance(val, dict):
            result.update(normalize_dict(val))
        else:
            result[key] = val

    return result


sample_dict = {
    "key1": "val1",
    "key2": {
        "key2_1": "val2_1",
        "key2_2": {
            "key2_2_1": "val2_2_1",
            "key2_2_2": "val2_2_2",
        },
        "key2_3": "val2_3"
    },
    "key3": "val3",
    "key4": "val4"
}

output_dict = normalize_dict(sample_dict)
print(output_dict)
