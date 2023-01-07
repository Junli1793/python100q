"""
Python | Output Formatting
https://www.geeksforgeeks.org/python-output-formatting/

There are several ways to format output.

    1, To use formatted string literals, begin a string with f or F before the opening quotation mark or triple quotation mark.
    2, The str. format() method of strings helps a user create a fancier output
    3, Users can do all the string handling by using string slicing and concatenation operations to create any layout that the users want.
    The string type has some methods that perform useful operations for padding strings to a given column width.
    4, Formatting output using String modulo operator(%)

"""
import json
from pprint import pformat

print()
print("==============Example 1: modulo operator(%)==============")
# print integer and float value
print("Geeks : %2d, Portal : %5.2f" % (1, 05.333))

# print integer value
print("Total students : %3d, Boys : %2d" % (240, 120))

# print octal value
print("%7.3o" % 25)

# print exponential value
print("%10.3E" % 356.08977)

print()
print("==============Example 2: format==============")

# using format() method
print('I love {} for "{}!"'.format('Geeks', 'Geeks'))

# using format() method and referring
# a position of the object
print('{0} and {1}'.format('Geeks', 'Portal'))

print('{1} and {0}'.format('Geeks', 'Portal'))

# the above formatting can also be done by using f-Strings
# Although, this features work only with python 3.6 or above.
g = 'geeks'
G = 'Geeks'
print(f"I love {g} for \"{G}!\"")
print(f"{'Geeks'} and {'Portal'}")

print()
print("combining positional and keyword arguments")
print('Number one portal is {0}, {1}, and {other}.'.format('Geeks', 'For', other='Geeks'))

# using format() method with number
print("Geeks :{0:2d}, Portal :{1:8.2f}".format(12, 00.546))

# Changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42, 11))

print("Geeks: {a:5d},  Portal: {p:8.2f}".format(a=453, p=59.058))

print()
print("using format() in dictionary")
tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678}

print('Geeks: {0[geeks]:d}; For: {0[for]:d}; Geeks: {0[geek]:d}'.format(tab))

data = dict(fun="GeeksForGeeks", adj="Portal")

# using format() in dictionary
print("I love {fun} computer {adj}".format(**data))

print()
print("==============Example 3: String method==============")

cstr = "I love geeksforgeeks"

# Printing the center aligned
# string with fillchr
print("Center aligned string with fillchr: ")
print(cstr.center(40, '#'))

# Printing the left aligned
# string with "-" padding
print("The left aligned string is : ")
print(cstr.ljust(40, '-'))

# Printing the right aligned string
# with "-" padding
print("The right aligned string is : ")
print(cstr.rjust(40, '-'))

# 返回长度为 width 的字符串，原字符串右对齐，前面填充0
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

print()
print("==============Example 4: pprint.pformat()==============")

data = """{
	"Name": "Jennifer Smith",
	"Contact Number": 7867567898,
	"Email": "jen123@gmail.com",
	"Hobbies":["Reading", "Sketching", "Horse Riding"]
	}"""

print(type(data))

print("parsing string to JSON (dict)")
json_obj = json.loads(data)
print(type(json_obj))
print(pformat(json_obj))

print()
print("==============Example 5: 原始字符串 r''==============")

print(r"\n")
print("\n")
print("\t", R"\n")
