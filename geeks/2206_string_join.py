#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

语法：
    str.join(sequence)

    sequence -- 要连接的元素序列。

    返回值
    返回通过指定字符连接序列中元素后生成的新字符串。

"""

print()
print("==============Example 1: join string==============")

jn1 = "-"
jn2 = "------"
str1 = 'name'

print("字符串也属于序列")
print(jn1.join(str1))

print("使用多字符连接序列")
print(jn2.join(str1))

print()
print("==============Example 2: join set==============")

fruits = {'apple', 'banana'}
print(jn1.join(fruits))  # 连接的序列是集合

print()
print("==============Example 3: join tuple==============")

animals = ("pig", "dog")
print(jn1.join(animals))  # 连接的序列是元祖

print()
print("==============Example 4: join dict==============")

students = {"name1": "joy", "name2": "john", "name3": "jerry"}  # 连接的序列是字典，会将所有key连接起来
print(jn1.join(students))
print(jn1.join(students.keys()))
print(jn1.join(students.values()))

print()
print("==============Example 5: join list==============")
fruits = ["apple", "Orange", "Kiwi", "banana", "cherry"]
print(jn2.join(fruits))
