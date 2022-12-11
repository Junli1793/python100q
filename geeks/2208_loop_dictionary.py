"""
Python - Loop Dictionaries
https://www.w3schools.com/python/python_dictionaries_loop.asp

"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

###########
# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, the return value are the keys of the dictionary,
# but there are methods to return the values as well.
###########
print(thisdict)

for x in thisdict:
    print(x, end=' => ')
    print(thisdict[x])

for x in thisdict.values():
    print(x)

for x in thisdict.keys():
    print(x)

print(">>>thisdict.items() is a view object")
"""
Python 字典 items() 方法以列表返回视图对象，是一个可遍历的key/value 对。
dict.keys()、dict.values() 和 dict.items() 返回的都是视图对象（view objects），提供了字典实体的动态视图，这就意味着字典改变，视图也会跟着变化。

视图对象（view objects）不是列表，不支持索引，可以使用 list() 来转换为列表。
我们不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。

"""
for x, y in thisdict.items():
    print(x, y)

print()
print(type(thisdict.items()))
print(thisdict.items())
print(list(thisdict.items()))
print()

print(">>>Change Values")
thisdict["year"] = 2018
print(thisdict)

print(">>>Update Dictionary")
thisdict.update({"year": 2020})
print(thisdict)
thisdict.update({"color": "red"})
print(thisdict)
