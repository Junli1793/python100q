#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
描述
dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。

dir 语法：
    dir([object])

 参数说明：
    object -- 对象、变量、类型。


"""


print()
print("==============Example 1: module==============")

print(dir())

print()
print("==============Example 2: list==============")

print(dir([]))

print()
print("==============Example 3: tuple==============")

print(dir((1,)))

print()
print("==============Example 4: dict==============")

print(dir({}))

print()
print("==============Example 5: set==============")

print(dir({1}))

print()
print("==============Example 5: int==============")

print(dir(1))

print()
print("==============Example 5: string==============")

print(dir("1"))
