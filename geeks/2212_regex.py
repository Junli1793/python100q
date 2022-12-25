"""
Python RegEx
https://www.w3schools.com/python/python_regex.asp

A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

The re module offers a set of functions that allows us to search a string for a match:
findall 	Returns a list containing all matches
search 	    Returns a Match object if there is a match anywhere in the string
split 	    Returns a list where the string has been split at each match
sub 	    Replaces one or many matches with a string

https://www.runoob.com/python3/python3-reg-expressions.html
https://www.runoob.com/regexp/regexp-tutorial.html

"""

import re

"""
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，则返回元组列表，如果没有找到匹配的，则返回空列表。

注意： match 和 search 是匹配一次 findall 匹配所有。

语法格式为：
    re.findall(pattern, string, flags=0)
    或
    pattern.findall(string[, pos[, endpos]])

"""

print("==============Example 1: findall==============")

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
x = re.findall(r"a.n", txt)
print(x)

x = re.findall("Portugal", txt)
print(x)

string = """Hello my Number is 123456789 and
    my friend's number is 987654321"""

regex = r'\d+'
matchs = re.findall(regex, string)
print(matchs)

print()
print("==============Example 2: search==============")

"""
re.search 扫描整个字符串并返回第一个成功的匹配。

注意： match 和 search 是匹配一次 findall 匹配所有。

函数语法：
    re.search(pattern, string, flags=0)
    
"""

print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配

x = re.search(r"\s", txt)
print(x)
print("The first white-space character is located in position:", x.start())
print("The first white-space character is located in position:", x.end())

# A Python program to demonstrate working of re.match().
# import re

# Lets use a regular expression to match a date string
# in the form of Month name followed by day number
regex = r"([a-zA-Z]+) (\d+)"

matchs = re.search(regex, "I was born on June 24")

if matchs != None:

    # We reach here when the expression "([a-zA-Z]+) (\d+)"
    # matches the date string.

    # This will print [14, 21), since it matches at index 14
    # and ends at 21.
    print("Match at index % s, % s" % (matchs.start(), matchs.end()))

    # We us group() method to get all the matches and
    # captured groups. The groups contain the matched values.
    # In particular:
    # match.group(0) always returns the fully matched string
    # match.group(1) match.group(2), ... return the capture
    # groups in order from left to right in the input string
    # match.group() is equivalent to match.group(0)

    # So this will print "June 24"
    print("Full match: % s" % (matchs.group(0)))

    # So this will print "June"
    print("Month: % s" % (matchs.group(1)))

    # So this will print "24"
    print("Day: % s" % (matchs.group(2)))

else:
    print("The regex pattern does not match.")

print()
print("==============Example 3: split==============")

###########
# The split() Function
# The split() function returns a list where the string has been split at each match.
###########
print(txt)
x = re.split(r"\s", txt)
print(type(x))
print(x)

x = re.split(r"\s", txt, 1)
print(x)

# example 1
print()
from re import split

# '\W+' denotes Non-Alphanumeric Characters
# or group of characters Upon finding ','
# or whitespace ' ', the split(), splits the
# string from that point
print(split(r'\W+', 'Words, words , Words'))
print(split(r'\W+', "Word's words Words"))

# Here ':', ' ' ,',' are not AlphaNumeric thus,
# the point where splitting occurs
print(split(r'\W+', 'On 12th Jan 2016, at 11:02 AM'))

# '\d+' denotes Numeric Characters or group of
# characters Splitting occurs at '12', '2016',
# '11', '02' only
print(split(r'\d+', 'On 12th Jan 2016, at 11:02 AM'))

# example 2
print()
# import re

# Splitting will occurs only once, at
# '12', returned list will have length 2
print(re.split(r'\d+', 'On 12th Jan 2016, at 11:02 AM', 1))

# 'Boy' and 'boy' will be treated same when
# flags = re.IGNORECASE
print(re.split(r'[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))
print(re.split(r'[a-f]+', 'Aey, Boy oh boy, come here'))

print()
print("==============Example 4: sub==============")

###########
# re.sub()
# The ‘sub’ in the function stands for SubString,
# a certain regular expression pattern is searched in the given string(3rd parameter),
# and upon finding the substring pattern is replaced by repl(2nd parameter),
# count checks and maintains the number of times this occurs.
###########
# import re

# Regular Expression pattern 'ub' matches the
# string at "Subject" and "Uber". As the CASE
# has been ignored, using Flag, 'ub' should
# match twice with the string Upon matching,
# 'ub' is replaced by '~*' in "Subject", and
# in "Uber", 'Ub' is replaced.
print(re.sub(r'ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))

# Consider the Case Sensitivity, 'Ub' in
# "Uber", will not be replaced.
print(re.sub(r'ub', '~*', 'Subject has Uber booked already'))

# As count has been given value 1, the maximum
# times replacement occurs is 1
print(re.sub(r'ub', '~*', 'Subject has Uber booked already', count=1, flags=re.IGNORECASE))

# 'r' before the pattern denotes RE, \s is for
# start and end of a String.
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))
print(re.sub(r'\bAND\b', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))

print()
print("==============Example 5: match==============")
"""
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

注意： match 和 search 是匹配一次 findall 匹配所有。

函数语法：
    re.match(pattern, string, flags=0)
    
"""

print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('www', 'www.runoob.com').start())  # 在起始位置匹配
print(re.match('www', 'www.runoob.com').end())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配

print()
line = "Cats are smarter than dogs"

searchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
# searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")

print()
matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print("search --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

print()
print("==============Example 6: compile==============")

"""
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

语法格式为：
    re.compile(pattern[, flags])
    
"""

pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
print(m)

m = pattern.match('one12twothree34four', 2, 10)  # 从'e'的位置开始匹配，没有匹配
print(m)

m = pattern.match('one12twothree34four', 3, 18)  # 从'1'的位置开始匹配，正好匹配
print(m)
print()
print(m.group())
print(m.start())
print(m.end())
print(m.span())

print()
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')
print(m)
print(m.group(0))
print(m.span(0))
print(m.group(1))
print(m.span(1))
print(m.group(2))
print(m.span(2))
print(m.groups())
# print(m.group(3))

print()
pattern = re.compile(r'(w[a-z]+) (w[a-z]+) (w[a-z]+)', re.I)  # re.I 表示忽略大小写
m = pattern.findall('Hello World Wide Web, Hello World Wide Web, Hello World Wide Web')
print(m)
print(m[0])
print(m[1])
print(m[2])
print(m[0][0])
print(m[0][1])
print(m[0][2])

