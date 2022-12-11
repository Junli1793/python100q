"""
Python Tuples
https://www.w3schools.com/python/python_tuples.asp

Tuples are used to store multiple items in a single variable.

A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.

"""

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple)
print(len(thistuple))
print(type(thistuple))

print()
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])   # no thistuple[5]
print(thistuple[:4])    # no thistuple[4]
print(thistuple[2:])
print(thistuple[-4:-1]) # no thistuple[-1]
print(thistuple[2:10])

print()
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
print()

"""
If the number of variables is less than the number of values, 
you can add an * to the variable name and the values will be assigned to the variable as a list.
"""

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

###########
# Loop Through a Tuple
###########
print()
for x in fruits:
    print(x)

print()
for i in range(len(fruits)):
    print(fruits[i])

print()
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

