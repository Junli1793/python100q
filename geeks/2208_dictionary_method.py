#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：
    d = {key1 : value1, key2 : value2, key3 : value3 }

注意:
    1, 键必须是唯一的，但值则不必。
    2, 值可以取任何数据类型，但键必须是不可变的，如字符串，数字。

Python字典包含了以下内置函数：
    len(dict)   计算字典元素个数，即键的总数。
    str(dict)   输出字典，可以打印的字符串表示。
    type(variable)  返回输入的变量类型，如果变量是字典就返回字典类型。

Python字典包含了12个内置方法

"""

print()
print("==============Example 0: dict.fromkeys(seq[, value])==============")

d = {}
print(d)
print("Length:", len(d))
print(type(d))

seq = ('rice', 'bread', 'noodle')
d0 = dict.fromkeys(seq, 200)
print(d0)
print("Length:", len(d0))

print()
print("==============Example 1: dict.update(dict2)==============")

d1 = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}

d.update(d0)
print(d)
print("Length:", len(d))

d.update(d1)
print(d)
print("Length:", len(d))

print()
print("==============Example 2: key in dict==============")

print('eggs' in d)
print('pork' in d)
print(200 not in d)

print()
print("==============Example 3: dict.keys(), dict.values() and dict.items()==============")

"""
Python 字典 items() 方法以列表返回视图对象，是一个可遍历的key/value 对。
dict.keys()、dict.values() 和 dict.items() 返回的都是视图对象（ view objects），提供了字典实体的动态视图，这就意味着字典改变，视图也会跟着变化。

视图对象不是列表，不支持索引，可以使用 list() 来转换为列表。

我们不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。

"""

keys = d.keys()
values = d.values()
items = d.items()

print(type(keys))
print(type(values))
print(type(items))

for key in keys:
    print(key, type(key))

for value in values:
    print(value, type(value))

for item in items:
    print(item, type(item))

print()
print("==============Example 4: dict.get(key[, value]) and dict.setdefault(key, default=None)==============")

print("get(key) 返回指定键的值，如果键不在字典中返回默认值 None 或者设置的默认值。")
print("rice : ", d.get('rice'))
print("rice : ", d['rice'])

print("pork : ", d.get('pork'))
print("pork : ", d.get('pork', 1000))

try:
    print("pork : ", d['pork'])
except KeyError as err:
    print("KeyError occurs: ", err)

print(d)

print()
print("setdefault(key) 如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None。")
print("pork : ", d.setdefault('pork', 1000))
print(d)

print("beef : ", d.setdefault('beef'))
print(d)

print()
print("==============Example 5: popitem() and pop(key[,default])==============")

print("popitem() 返回最后插入键值对(key, value 形式)，按照 LIFO（Last In First Out 后进先出法） 顺序规则，即最末尾的键值对。")
element = d.popitem()
print(type(element))
print(element)
print(d)
print()

print("pop(key) 返回被删除的值")
print("如果 key 存在 - 删除字典中对应的元素")
print("d.pop('eggs')")
element = d.pop('eggs')
print(type(element))
print(element)
print(d)
print()

print("如果 key 不存在 - 返回设置指定的默认值 default")
print("d.pop('beef', 1000)")
element = d.pop('beef', 1000)
print(type(element))
print(element)
print(d)
print()

print("如果 key 不存在且默认值 default 没有指定 - 触发 KeyError 异常")
print("d.pop('beef')")
try:
    element = d.pop('beef')
except KeyError as err:
    print("KeyError occurs: ", err)
print(d)

print()
print("==============Example 6: dict.copy() and dict.clear()==============")

d2 = d.copy()
print("新字典为: ", d2)
print("原字典为: ", d)

print("新字典id: ", id(d2))
print("原字典id: ", id(d))
print()

d2.clear()
print("d2.clear()")
print("d2: ", d2)
print("d: ", d)
print()

d.clear()
print("d.clear()")
print("d: ", d)
