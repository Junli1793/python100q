"""
Python Tuples
https://www.w3schools.com/python/python_tuples.asp

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered, unchangeable and allow duplicate values.
Tuples are written with round brackets.

"""

tuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple1)

print()
print("==============Example 0: new tuple without ()==============")

tuple0 = "a", "b", "c", "d"
print(">>>tuple0")
print(tuple0)
print(type(tuple0))
print()

tuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(">>>tuple1")
print(tuple1)

print()
print("==============Example 1: len()==============")

print(len(tuple1))
print(type(tuple1))

print()
print("==============Example 2: slice==============")

print("l[i:j:s] => l[start:end:step]")
print("当i缺省时，默认为0，即 a[:4]相当于 a[0:4]")
print("当j缺省时，默认为len(alist), 即a[2:]相当于a[2:10]")
print("当i,j都缺省时，a[:]就相当于完整复制一份a")
print("s<0时，i缺省时，默认为-1， j缺省时，默认为-len(a)-1")

print("tuple1[:4]".rjust(20, ' '), tuple1[:4])  # no tuple1[4]
print("tuple1[2:]".rjust(20, ' '), tuple1[2:])
print("tuple1[:]".rjust(20, ' '), tuple1[:])
print("tuple1[::2]".rjust(20, ' '), tuple1[::2])
print("tuple1[::-1]".rjust(20, ' '), tuple1[::-1])
print()

print("tuple1[1]".rjust(20, ' '), tuple1[1])
print("tuple1[-1]".rjust(20, ' '), tuple1[-1])
print("tuple1[2:5]".rjust(20, ' '), tuple1[2:5])  # no tuple1[5]
print("tuple1[-4:-1]".rjust(20, ' '), tuple1[-4:-1])  # no tuple1[-1]
print()

print("tuple1[2:10]".rjust(20, ' '), tuple1[2:10])  # equal to tuple1[2:]

print()
print("==============Example 3: tuple with only one item==============")

tuple2 = ("apple",)
print("tuple2 ", tuple2)
print(type(tuple2))
print()

tuple4 = "orange",
print("tuple4 ", tuple4)
print(type(tuple4))
print()

print("tuple3 is NOT a tuple")
tuple3 = ("banana")
print("tuple3 ", tuple3)
print(type(tuple3))
print()

print("tuple5 is NOT a tuple")
tuple5 = (100)
print("tuple5 ", tuple5)
print(type(tuple5))
print()

"""
If the number of variables is less than the number of values, 
you can add an * to the variable name and the values will be assigned to the variable as a list.
"""

print()
print("==============Example 4: assign tuple to tuple==============")

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
print("fruits[:]".rjust(20, ' '), fruits[:])

(green, yellow, *red) = fruits
print("green".rjust(20, ' '), green)
print("yellow".rjust(20, ' '), yellow)
print("*red".rjust(20, ' '), red)

(green, *tropic, red) = fruits
print("green".rjust(20, ' '), green)
print("*tropic".rjust(20, ' '), tropic)
print("red".rjust(20, ' '), red)

print()
print("==============Example 5: Loop Through a Tuple==============")

print(">>>iterator")
for x in fruits:
    print(x)

print()
print(">>>index with for loop")
for i in range(len(fruits)):
    print(fruits[i])

print()
i = 0
print(">>>index with while loop")
while i < len(fruits):
    print(fruits[i])
    i = i + 1

print()
print("==============Example 6: tuple + tuple==============")

a = (1, 2, 3)
print("a: ", a)
print("id(a) ", id(a))
b = (4, 5, 6)
a += b
print("a: ", a)
print("id(a) ", id(a))

print()
print("==============Example 7: tuple * 3==============")

b = a * 3
print(b)

print()
print("==============Example 8: check if item in tuple==============")
print(1 in b)
print(a in b)

print()
print("==============Example 9: convert tuple to list==============")

t1 = (1, 2, 4, 5)
print("t1: ", t1)
print("id(t1) ", id(t1))
print()

t1 = t1[:2] + (3,) + t1[2:]
print("t1: ", t1)
print("id(t1) ", id(t1))
print()

l1 = list(t1)
print("convert tuple to list")
print("l1: ", l1)
print()

print("change item of list")
l1[0] = 9
print("l1: ", l1)
print()

t1 = tuple(l1)
print("convert list to tuple again")
print("t1: ", t1)
print("id(t1) ", id(t1))

print()
print("==============Example 10: list in tuple can change==============")
t10 = (1, [3, 2])
t10[1][0] = 1
print("t10: ", t10)

t10[1].append(3)
print("t10: ", t10)

del t10[1][2]
print("t10: ", t10)


print()
print("==============Example 11: del tuple==============")

print("t10: ", t10)
try:
    del t10[0]
except TypeError as err:
    print("TypeError occurs: ", err)

try:
    del t10[1]
except TypeError as err:
    print("TypeError occurs: ", err)

del t10
try:
    print("删除后的元组 t10: ")
    print(t10)
except NameError as err:
    print("NameError occurs: ", err)
