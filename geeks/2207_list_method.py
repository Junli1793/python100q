#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
Python 已经内置确定序列的长度以及确定最大和最小的元素的方法。
    len(list)   列表元素个数
    max(list)   返回列表元素最大值
    min(list)   返回列表元素最小值
    list(seq)   将元组转换为列表

Python列表包含11个方法

"""

print()
print("==============Example 1: list.append(obj)==============")

print("append() 方法用于在列表末尾添加新的对象。")
list1 = ['Google', 'Runoob', 'Taobao']
print("原列表: ", list1)
list1.append('Baidu')
print("更新后的列表: ", list1)

list1.append([i for i in range(5)])
print("更新后的列表: ", list1)

print()
print("==============Example 2: list.extend(seq)==============")

print("extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。")
print("原列表: ", list1)
list2 = list(range(5))  # 创建 0-4 的列表

list1.extend(list2)  # 扩展列表
print("扩展后的列表: ", list1)

print()
print("==============Example 3: list.count(obj)==============")

print("Taobao 元素个数: ", list1.count("Taobao"))
print("list2 元素个数: ", list1.count(list2))

print()
print("==============Example 4: list.index(x[, start[, end]])==============")

print("Taobao 索引值为: ", list1.index("Taobao"))
print("list2 索引值为: ", list1.index(list2))

print()
print("==============Example 5: list.insert(index, obj)==============")

list1.insert(1, 'Baidu')
print('列表插入元素后为: ', list1)
print("Baidu 元素个数: ", list1.count("Baidu"))
print("Baidu 索引值为: ", list1.index("Baidu", 2))

print()
print("==============Example 6: list.pop([index=-1])==============")

list1.pop()
print("列表现在为: ", list1)
list1.pop(5)
print("列表现在为: ", list1)

print()
print("==============Example 7: list.remove(obj)==============")

list1.remove('Taobao')
print("列表现在为: ", list1)
list1.remove('Baidu')
print("列表现在为: ", list1)

print()
print("==============Example 8: list.reverse()==============")

list1.reverse()
print("列表反转后: ", list1)

print()
print("==============Example 9: list.sort( key=None, reverse=False)==============")

list1.sort(key=str)
print("列表排序后: ", list1)

list1.sort(key=str, reverse=True)
print("列表反向排序后: ", list1)

print()
print("==============Example 10: list.copy()==============")

list2 = list1.copy()
print("新的列表list2: ", list2)
print("list1 的地址: ", id(list1))
print("list2 的地址: ", id(list2))

print()
print("==============Example 11: list.clear()==============")

print("clear() 函数用于清空列表，类似于 del a[:]")
list1.clear()
print("list1列表清空后: ", list1, list2)
del list2[:]
print("list2列表清空后: ", list1, list2)
