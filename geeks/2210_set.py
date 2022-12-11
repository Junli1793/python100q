
"""
Python Sets
https://www.w3schools.com/python/python_sets.asp

Sets are used to store multiple items in a single variable.

A set is a collection which is unordered, unchangeable*, and unindexed.
Set items are unordered, unchangeable, and do not allow duplicate values.

* Note: Set items are unchangeable, but you can remove items and add new items.
"""

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
print(len(thisset))

# It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
print()

# Add
thisset.add("orange")
print(thisset)

# update with set
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# update with Any Iterable
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = thisset.union(set1).union(set2)
print(set3)

# Loop Items
for x in set3:
    print(x)
