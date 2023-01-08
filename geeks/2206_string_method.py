#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
python3 共有40个常用内建函数
    'capitalize', 'title', 'swapcase', 'upper', 'lower',
    'center', 'ljust', 'lstrip', 'rstrip', 'rjust', 'zfill',
    'count', 'index', 'rindex', 'find', 'rfind', 'endswith', 'startswith',
    'encode',
    'maketrans',
    'expandtabs',
    'format', 'format_map',
    'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'islower', 'isnumeric', 'isspace', 'istitle', 'isupper',
    'join',
    'split', 'splitlines', 'strip', 'rsplit',
    'replace'

"""

print()
print("==============Example 1: 大小写相关方法==============")

str1 = "this is string Example From Runoob....wow!!!"
print("str1: ".rjust(30), str1)
print("str1.capitalize(): ".rjust(30), str1.capitalize())
print("str1.lower(): ".rjust(30), str1.lower())
print("str1.upper(): ".rjust(30), str1.upper())
print("str1.swapcase(): ".rjust(30), str1.swapcase())
print("str1.title(): ".rjust(30), str1.title())
print()

print()
print("==============Example 2: 剥皮填充相关方法==============")

str2 = "*****this is **string** example....wow!!!*****"
print("str2: ".rjust(30), str2)
print("str2.strip('*'): ".rjust(30), str2.strip('*'), "(在字符串上执行 lstrip()和 rstrip())")
print("str2.rstrip('*'): ".rjust(30), str2.rstrip('*'), "(删除字符串末尾的空格或指定字符)")
print("str2.lstrip('*'): ".rjust(30), str2.lstrip('*'), "(截掉字符串左边的空格或指定字符)")
print()

str2 = "[runoob]"
print("\"[runoob]\".center(50, '*'): ".rjust(30), str2.center(50, '*'), "(The fill character must be exactly one character long)")
print("\"[runoob]\".ljust(50, '*'): ".rjust(30), str2.ljust(50, '#'), "(The fill character must be exactly one character long)")
print("\"[runoob]\".rjust(50, '*'): ".rjust(30), str2.rjust(50, '$'), "(The fill character must be exactly one character long)")
print("\"[runoob]\".zfill(50): ".rjust(30), str2.zfill(50), "(zfill() takes exactly one argument)")
print()

print()
print("==============Example 3: 定位计数相关方法==============")

print("len(str1): ".rjust(30), len(str1))
print()

print("str1.count('Run', 0, 10): ".rjust(30), str1.count("Run", 0, 10))
print("str1.count('Run', 0, 40): ".rjust(30), str1.count("Run", 0, 40))
print("str1.count('o', 0, 40): ".rjust(30), str1.count("o", 0, 40))
print()

print("str1: ".rjust(30), str1)
suffix = '!!'
print('suffix: '.rjust(30), suffix)
print("str1.find(suffix): ".rjust(30), str1.find(suffix))
print("str1.endswith(suffix): ".rjust(30), str1.endswith(suffix), "(从下标0开始)")
print("str1.endswith(suffix, 30): ".rjust(30), str1.endswith(suffix, 30), "(从下标30开始)")
print("str1.startswith(\"!!\"): ".rjust(30), str1.startswith("!!"), "str.startswith(substr, beg=0, end=len(string))")
print("str1.endswith(\"!!\"): ".rjust(30), str1.endswith("!!"), "str.endswith(suffix[, start[, end]])")
print()

suffix = 'Run'
print("str1: ".rjust(30), str1)
print('suffix: '.rjust(30), suffix)
print("str1.startswith(suffix, 20): ".rjust(30), str1.startswith(suffix, 20), "str.startswith(substr, beg=0, end=len(string))")
print("str1.startswith(suffix, 28): ".rjust(30), str1.startswith(suffix, 28), "str.startswith(substr, beg=0, end=len(string))")
print("str1.endswith(suffix): ".rjust(30), str1.endswith(suffix), "(从下标0开始)")
print("str1.endswith(suffix, 0, 31): ".rjust(30), str1.endswith(suffix, 0, 31))

print("str1: ".rjust(30), str1)
print("str1.find(suffix): ".rjust(30), str1.find(suffix), "(从下标0开始)")
print("str1.find(suffix, 20): ".rjust(30), str1.find(suffix, 20), "(从下标20开始)")
print("str1.find(suffix, 10, 20): ".rjust(30), str1.find(suffix, 10, 20), "（find()找不到会返回-1）")
print("str1.find(suffix, 10, 31): ".rjust(30), str1.find(suffix, 10, 31))

print("str1.index(suffix): ".rjust(30), str1.index(suffix), "(从下标0开始)")
print("str1.index(suffix, 20): ".rjust(30), str1.index(suffix, 20), "(从下标20开始)")
try:
    print("str1.index(suffix, 10, 20): ".rjust(30), str1.index(suffix, 10, 20))
except ValueError as err:
    print("str1.index(suffix, 10, 20): ".rjust(30), f"ValueError occurs: {err}", "(index()找不到会报错)")
print("str1.index(suffix, 10, 31): ".rjust(30), str1.index(suffix, 10, 31))
print()

print("str1: ".rjust(30), str1)
print("str1.find('is'): ".rjust(30), str1.find('is'), "(从下标0开始找)")
print("str1.index('is'): ".rjust(30), str1.index('is'), "(从下标0开始找)")
print("str1.rfind('is'): ".rjust(30), str1.rfind('is'), "(从右边开始找)")
print("str1.rindex('is'): ".rjust(30), str1.rindex('is'), "(从右边开始找)")

print()
print("==============Example 4: 编码解码相关方法==============")

str3 = "菜鸟教程"
print("str3: ".rjust(30), str3)

str_utf8 = str3.encode("UTF-8")
str_gbk = str3.encode("GBK")
print("str3.encode(UTF-8): ".rjust(30), str_utf8)
print("str3.encode(GBK): ".rjust(30), str_gbk)

print("UTF-8 decode(): ".rjust(30), str_utf8.decode('UTF-8', 'strict'))
print("GBK decode(): ".rjust(30), str_gbk.decode('GBK', 'strict'))

print()
print("==============Example 5: 数据类型测试相关方法==============")

str5 = "runoob2016"  # 字符串没有空格
print('str5: '.rjust(30), str5)
print("str5.isalnum(): ".rjust(30), str5.isalnum(), "isalnum()方法检测字符串是否由字母和数字组成。")
print("str5.isalpha(): ".rjust(30), str5.isalpha(), "isalpha()方法检测字符串是否只由字母或文字组成。")
print("str5.isdigit(): ".rjust(30), str5.isdigit(), "isdigit()方法检测字符串是否只由数字组成。")
print("str5.isdecimal(): ".rjust(30), str5.isdecimal(), "isdecimal()方法检查字符串是否只包含十进制字符。")
print("str5.islower(): ".rjust(30), str5.islower(), "islower()方法检测字符串是否由小写字母组成。")
print("str5.isupper(): ".rjust(30), str5.isupper(), "isupper()方法检测字符串中所有的字母是否都为大写。")
print("str5.isnumeric(): ".rjust(30), str5.isnumeric(), "isnumeric()方法检测字符串是否只由数字组成，数字可以是： Unicode 数字，全角数字（双字节），罗马数字，汉字数字。")
print("str5.isspace(): ".rjust(30), str5.isspace(), "isspace()方法检测字符串是否只由空白字符组成。(\\t\\r\\n)")
print("str5.istitle(): ".rjust(30), str5.istitle(), "istitle()方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。")
print()

str6 = "www.runoob.com"
print('str6: '.rjust(30), str6)
print("str6.isalnum(): ".rjust(30), str6.isalnum(), "isalnum()方法检测字符串是否由字母和数字组成。")
print("str6.isalpha(): ".rjust(30), str6.isalpha(), "isalpha()方法检测字符串是否只由字母或文字组成。")
print("str6.isdigit(): ".rjust(30), str6.isdigit(), "isdigit()方法检测字符串是否只由数字组成。")
print("str6.isdecimal(): ".rjust(30), str6.isdecimal(), "isdecimal()方法检查字符串是否只包含十进制字符。")
print("str6.islower(): ".rjust(30), str6.islower(), "islower()方法检测字符串是否由小写字母组成。")
print("str6.isupper(): ".rjust(30), str6.isupper(), "isupper()方法检测字符串中所有的字母是否都为大写。")
print("str6.isnumeric(): ".rjust(30), str6.isnumeric(), "isnumeric()方法检测字符串是否只由数字组成，数字可以是： Unicode 数字，全角数字（双字节），罗马数字，汉字数字。")
print("str6.isspace(): ".rjust(30), str6.isspace(), "isspace()方法检测字符串是否只由空白字符组成。(\\t\\r\\n)")
print("str6.istitle(): ".rjust(30), str6.istitle(), "istitle()方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。")
print()

str7 = "runoob菜鸟教程"
print('str7: '.rjust(30), str7)
print("str7.isalnum(): ".rjust(30), str7.isalnum(), "isalnum()方法检测字符串是否由字母和数字组成。")
print("str7.isalpha(): ".rjust(30), str7.isalpha(), "isalpha()方法检测字符串是否只由字母或文字组成。")
print("str7.isdigit(): ".rjust(30), str7.isdigit(), "isdigit()方法检测字符串是否只由数字组成。")
print("str7.isdecimal(): ".rjust(30), str7.isdecimal(), "isdecimal()方法检查字符串是否只包含十进制字符。")
print("str7.islower(): ".rjust(30), str7.islower(), "islower()方法检测字符串是否由小写字母组成。")
print("str7.isupper(): ".rjust(30), str7.isupper(), "isupper()方法检测字符串中所有的字母是否都为大写。")
print("str7.isnumeric(): ".rjust(30), str7.isnumeric(), "isnumeric()方法检测字符串是否只由数字组成，数字可以是： Unicode 数字，全角数字（双字节），罗马数字，汉字数字。")
print("str7.isspace(): ".rjust(30), str7.isspace(), "isspace()方法检测字符串是否只由空白字符组成。(\\t\\r\\n)")
print("str7.istitle(): ".rjust(30), str7.istitle(), "istitle()方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。")

print()
print("==============Example 6: 分割替换相关方法==============")

print("str1: ".rjust(30), str1)
print("str1.split(): ".rjust(30), str1.split())
print("str1.split('i'): ".rjust(30), str1.split('i'))
print("str1.split(' ', 2): ".rjust(30), str1.split(' ', 2), "str.split(str='', num=string.count(str))")
print("str1.replace('is', 'was'): ".rjust(30), str1.replace('is', 'was', 1), "str.replace(old, new[, max])")
print()

"""
splitlines() 按照行('\r', '\r\n', \n')分隔，
返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。

"""
print("splitlines()", 'ab c\n\nde fg\rkl\r\n'.splitlines())
print("splitlines()", 'ab c\n\nde fg\rkl\r\n'.splitlines(True), "str.splitlines([keepends])")

print()
print("==============Example 7: 其他方法==============")

print("max(str1): ".rjust(30), max(str1))
print("min(str1): ".rjust(30), min(str1))

str4 = "runoob\t12345\tabc"
print('原始字符串: '.rjust(30), str4)

# 默认 8 个空格
# runnob 有 6 个字符，后面的 \t 填充 2 个空格
# 12345 有 5 个字符，后面的 \t 填充 3 个空格
print('替换 \\t 符号: '.rjust(30), str4.expandtabs())

# 2 个空格
# runnob 有 6 个字符，刚好是 2 的 3 倍，后面的 \t 填充 2 个空格
# 12345 有 5 个字符，不是 2 的倍数，后面的 \t 填充 1 个空格
print('使用 2 个空格替换 \\t 符号: '.rjust(30), str4.expandtabs(2))
print('使用 3 个空格: '.rjust(30), str4.expandtabs(3))
print('使用 4 个空格: '.rjust(30), str4.expandtabs(4))
print('使用 5 个空格: '.rjust(30), str4.expandtabs(5))
print('使用 6 个空格: '.rjust(30), str4.expandtabs(6))

