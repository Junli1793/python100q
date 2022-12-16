#!/usr/bin/python3
# -*- coding: UTF-8 -*-


"""
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
"""

"""
======================
递归做，非常慢。计算n=36就要大概七八秒吧
"""
 
# def get_total (month):
#     if month == 1 or month == 2:
#         return 1
#     else:
#         return get_total(month - 1) + get_total(month - 2)
# 
# 
# lst = []
# for i in range(1, 36):
#     lst.append(get_total(i))
# #     print(get_total(i))
# 
# print(lst)
"""
======================
"""

# def fibon(n):
#     a = b = 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
# 
#         
# for x in fibon(64):
#     print(x)  

"""
======================
"""

   
def Rabbit(num):
    i = 1
    a, b = 1, 1
    while i <= num:
        yield a
        i += 1
        a, b = b, a + b
 
   
list1 = [x for x in Rabbit(36)]
print(list1)
 
for x in Rabbit(36):
    print(x)

"""
======================
"""
# a = 1
# b = 1
# for i in range(1, 36, 2):
#     print '%d %d' % (a, b),
#     a += b
#     b += a

"""
======================
"""

# f1 = 1
# f2 = 1
# for i in range(1, 36):
#     print '%12ld %12ld' % (f1, f2),
#     if (i % 3) == 0:
#         print ''
#     f1 = f1 + f2
#     f2 = f1 + f2
