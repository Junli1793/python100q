"""
Python Sets
https://www.w3schools.com/python/python_sets.asp

Sets are used to store multiple items in a single variable.

A set is a collection which is unordered, unchangeable*, and unindexed.
Set items are unordered, unchangeable, and do not allow duplicate values.

* Note: Set items are unchangeable, but you can remove items and add new items.

"""

print()
print("==============Example 0: type()==============")

set0 = {"apple", "banana", "cherry"}
print("set0", set0)
print(type(set0))

print()
print("==============Example 1: len()==============")

set1 = {"apple", "banana", "cherry", "apple"}
print("set1", set1)
print(len(set1))

# It is also possible to use the set() constructor to make a set.
print()
print("==============Example 2: set()==============")

print(">>>convert tuple to set")
set2 = set(("apple", "banana", "cherry"))
print("set2", set2)
print()

print(">>>convert list to set")
list1 = [1, 1, 2, 3, 4, 5, 3, 1, 4, 6, 5]
set3 = set(list1)
print("set3", set3)
print()

print(">>>convert tuple to set")
tuple1 = (2, 3, 5, 6, 3, 5, 2, 5)
set3 = set(tuple1)
print("set3", set3)
print()

print(">>>wrong way to convert string to set")
set4 = set('apple')
print("set4", set4)
print()

print(">>>correct way to convert string to set")
set4 = set(('apple',))
print("set4", set4)
print()

print()
print("==============Example 3: add element to set==============")
set2.add("orange")
print("set2", set2)

# update with set
print()
print("==============Example 4: update set with set==============")
tropical = {"pineapple", "mango", "papaya"}
set2.update(tropical)
print("set2", set2)

# update with Any Iterable
print()
print("==============Example 5: update set with Any Iterable==============")
mylist = ["kiwi", "orange"]
set2.update(mylist)
print("set2", set2)

# union
print()
print("==============Example 6: union 2 set==============")
set4 = {"a", "b", "c"}
set5 = {1, 2, 3}
set6 = set2.union(set4).union(set5)
print("set6", set6)

print()
print("==============Example 7: set.pop()==============")
print("set6.pop()", set6.pop())
print("set6", set6)

print()
print("==============Example 8: set.remove()==============")
print("set6.remove()", set6.remove('a'))
print("set6", set6)

print()
print("==============Example 9: set.discard()==============")
print("set6.discard()", set6.discard('b'))
print("set6", set6)

# Loop Items
print()
print("==============Example 10: Loop Items of set==============")
for x in set6:
    print(x)

print()
print("==============Example 11: set.clear()==============")
print("set6.clear()", set6.clear())
print("set6", set6)

print()
print("==============Example 12: in==============")

set12 = {x for x in 'abracadabra' if x not in 'abc'}
print("set12", set12)

print()
print("==============Example 13: 集合间的运算==============")

a = set('abracadabra')
b = set('alacazam')
print("a", a)
print("b", b)

print("集合a中包含而集合b中不包含的元素")
print("a - b", a - b)

print("集合a或b中包含的所有元素")
print("a | b", a | b)

print("集合a和b中都包含了的元素")
print("a & b", a & b)

print("不同时包含于a和b的元素")
print("a ^ b", a ^ b)
