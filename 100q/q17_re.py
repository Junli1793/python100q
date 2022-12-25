#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。

"""
import re

print()
print("==============Answer 1==============")

str1 = input("输入一行字符")
# woshiyankaidong12 a 22 33 ## $$ %%

count_l = 0
count_n = 0
count_s = 0
count_o = 0
for letter in str1:
    if re.match(r"[a-zA-Z]", letter):
        count_l += 1
    elif re.match(r"\s", letter):
        count_s += 1
    elif re.match(r"\d", letter):
        count_n += 1
    else:
        count_o += 1

print(f"letters : {count_l}")
print(f"numbers : {count_n}")
print(f"spaces : {count_s}")
print(f"other : {count_o}")

print()
print("==============Answer 2==============")

str = input('请输入一串字符：')

r1 = re.compile('[a-zA-Z]')
r2 = re.compile('[0-9]')
print('英文字母的个数为： %d' % len(re.findall(r1, str)))
print('数字的个数为： %d' % len(re.findall(r2, str)))
print('空格的个数为： %d' % len(re.findall(' ', str)))
print('其他字符的个数为： %d' % (len(str) - len(re.findall(r1, str)) - len(re.findall(r2, str)) - len(re.findall(' ', str))))

print()
print("==============Answer 3==============")

s = input('输入一串字符：')
char = re.findall(r'[a-zA-Z]', s)
num = re.findall(r'[0-9]', s)
blank = re.findall(r' ', s)
chi = re.findall(r'[\u4E00-\u9FFF]', s)
other = len(s) - len(char) - len(num) - len(blank) - len(chi)
print("字母：", len(char), "\n数字：", len(num), "\n空格：", len(blank), "\n中文：", len(chi), "\n其他：", other)

print()
print("==============Answer 4==============")

s = input('请输入一个字符串:\n')
print("开始统计...")
list1 = [0, 0, 0, 0]
temp = [lambda i: 1 if (i.isalpha()) else 0, lambda i: 1 if (i.isspace()) else 0, lambda i: 1 if (i.isdigit()) else 0]
for i in s:
    list1[0] += temp[0](i)  # 字母
    list1[1] += temp[1](i)  # 空格
    list1[2] += temp[2](i)  # 数字
    list1[3] = len(s) - list1[0] - list1[1] - list1[2]  # 特殊字符

print(list1)

print()
print("==============Answer 5==============")

s = input('请输入一个字符串:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print('char = %d,space = %d,digit = %d,others = %d' % (letters, space, digit, others))


print()
print("==============Answer 6==============")
# s = input('输入一串字符：')
s = "wo de ip dizhis 192.168.100.1, ni de ip dizhi shi 192.168.10.10"
# ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', s)
ips = re.findall(r'(?:\d{1,3}\.){3}\d{1,3}', s)
print(ips)
