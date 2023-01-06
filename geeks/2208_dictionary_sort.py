#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
Python3 sorted() 函数
https://www.runoob.com/python3/python3-func-sorted.html

sorted() 函数对所有可迭代的对象进行排序操作。
    sort 与 sorted 区别：
    1, sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
    2, list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

sorted 语法：
    sorted(iterable, cmp=None, key=None, reverse=False)

参数说明：
    1, iterable -- 可迭代对象。
    2, cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
    3, key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    4, reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

返回值:
    返回重新排序的列表。

"""
from pprint import pformat

print()
print("==============Example 1: sorted() function==============")

# sorted(iterable, key=None, reverse=False)
d1 = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
print(sorted(d1))
print(d1)

print()
print("==============Example 2: 复杂的实例==============")
s = "德国 10 11 16\n意大利 10 10 20\n荷兰 10 12 14\n法国 10 12 11\n英国 22 21 22\n中国 38 32 18\n日本 27 14 17\n美国 39 41 33" \
    "\n俄罗斯 20 28 23\n澳大利亚 17 7 22\n匈牙利 7 6 7\n加拿大 7 6 7\n古巴 7 3 5\n巴西 7 6 7\n新西兰 7 6 8"
s_to_list = s.split('\n', -1)

# dictionary
country_dict = {}

print(">>>parse s to list of list")
for i in range(len(s_to_list)):
    # 每一行数据
    data = s_to_list[i].split(' ')
    print(f"line {i}: {data}")
    # 组装数据结构
    # country_dict={'China': [-38, -32, -18], 'Russia': [-20, -28, -23]}
    country_dict[data[0]] = [int('-' + i) for i in data[1:]]

print()
print(">>>dictionary converted from list of list")
print(pformat(country_dict))
print()

print(">>>(x[1]代表奖牌数目, x[0]代表国家), 先以奖牌数排序(默认为升序)，奖牌数相同再以国家名排序")
new_country_list = sorted(country_dict.items(), key=lambda x: (x[1], x[0]))
print(pformat(new_country_list))
print()

rank_list = []
for country in new_country_list:
    rank_list.append((country[0]))

for rank in range(len(rank_list)):
    print(f"{(rank + 1):2d}  {rank_list[rank]}")
