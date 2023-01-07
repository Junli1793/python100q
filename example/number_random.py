#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
1, choice() 方法返回一个列表，元组或字符串的随机项。
    random.choice(seq)

    seq -- 可以是一个列表，元组或字符串。

2, randrange() 方法返回指定递增基数集合中的一个随机数，基数默认值为1。
    random.randrange ([start,] stop [,step])

    start -- 指定范围内的开始值，包含在范围内。
    stop -- 指定范围内的结束值，不包含在范围内。
    step -- 指定递增基数。

3, random() 方法返回随机生成的一个实数，它在半开放区间 [0,1) 范围内。
    random.random()

4， seed() 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。
    random.seed([x])

    x -- 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
    我们调用 random.random() 生成随机数时，每一次生成的数都是随机的。
    但是，当我们预先使用 random.seed(x) 设定好种子之后，其中的 x 可以是任意数字，如10，这个时候，先调用它的情况下，使用 random() 生成的随机数将会是同一个。

5， shuffle() 方法将序列的所有元素随机排序。
    random.shuffle(lst)

    lst -- 列表。

6, uniform() 方法将随机生成下一个实数，它在 [x,y] 范围内。
    random.uniform(x, y)

    x -- 随机数的最小值，包含该值。
    y -- 随机数的最大值，包含该值。

    返回一个浮点数 N，取值范围为如果 x<y 则 x <= N <= y，如果 y<x 则y <= N <= x。

"""
import random

print()
print("==============Example 1: random.choice(seq)==============")

print("从 range(100) 返回一个随机数 : ", random.choice(range(100)))
print("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))

print()
print("==============Example 2: random.randrange ([start,] stop [,step])==============")

print("从0-100中随机选取一个偶数")
print("randrange(0, 100, 2) : ", random.randrange(0, 100, 2))

print("从0-100中随机选取一个能被4整除的整数")
print("randrange(0, 100, 4) : ", random.randrange(0, 100, 4))

print("从0-100中随机选取一个能被3整除后余1的数")
print("randrange(0, 100, 3) : ", random.randrange(1, 100, 3))

print("从0-99选取一个随机数")
print("randrange(100) : ", random.randrange(100))

print()
print("==============Example 3: random.random()==============")

print("第一个随机数")
print("random(): ", random.random())

print("第二个随机数")
print("random(): ", random.random())

print()
print("==============Example 4: random.seed()==============")

random.seed()
print("使用默认种子生成随机数：", random.random())
print("使用默认种子生成随机数：", random.random())

random.seed(10)
print("使用整数 10 种子生成随机数：", random.random())
random.seed(10)
print("使用整数 10 种子生成随机数：", random.random())

random.seed("hello", 2)
print("使用字符串种子生成随机数：", random.random())
random.seed("hello", 2)
print("使用字符串种子生成随机数：", random.random())

random.seed(10)
print("使用整数 10 种子生成随机数：", random.random())

print()
print("==============Example 5: random.shuffle(lst)==============")

list1 = [20, 16, 10, 5]
random.shuffle(list1)
print("随机排序列表 : ", list1)

random.shuffle(list1)
print("随机排序列表 : ", list1)

SEED = 10
original_list = ['list', 'elements', 'go', 'here']
random.seed(SEED)
print("需要重置列表")
my_list = original_list[:]
random.shuffle(my_list)
print("RUN1: ", my_list)

random.seed(SEED)
print("需要重置列表")
my_list = original_list[:]
random.shuffle(my_list)
print("RUN2: ", my_list)

print()
print("==============Example 6: random.uniform(x, y)==============")

print("uniform(5, 10)的随机浮点数: ", random.uniform(5, 10))
print("uniform(7, 14)的随机浮点数: ", random.uniform(7, 14))
print("uniform(5, 10)的随机浮点数, 并保留两位小数: ", round(random.uniform(5, 10), 2))

print()
print("==============Example 7: random.randint(x, y)==============")

print("randint(5, 10)的整型随机数: ", random.randint(5, 10))
print("randint(7, 14)的整型随机数: ", random.randint(7, 14))

print()
print("==============Example 8: random.sample(lst, n)==============")

print("从 range(100) 返回一个随机数 : ", random.sample(range(100), 1))
print("从列表中 [1, 2, 3, 5, 9]) 返回二个随机元素 : ", random.sample([1, 2, 3, 5, 9], 2))
print("从字符串中 'Hello Runboo!' 返回三个随机字符 : ", random.sample('Hello Runboo!', 3))
