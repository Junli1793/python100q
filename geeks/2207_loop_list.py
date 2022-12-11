"""
Python - Loop Lists
https://www.w3schools.com/python/python_lists_loop.asp

"""

###########
# Method 1: for loop
# We can also use a for loop to iterate through an iterable object
# (that is either a list, a tuple, a dictionary, a set, or a string).
# The for loop actually creates an iterator object and executes the next() method for each loop.
###########
thislist = ["apple", "banana", "cherry"]
print(thislist)
for x in thislist:
    print(x)


###########
# Method 2: Loop Through the Index Numbers
###########
thislist = ["apple", "banana", "cherry"]
print(thislist)
for i in range(len(thislist)):
    print(thislist[i])


###########
# Method 3: Using a While Loop
###########
thislist = ["apple", "banana", "cherry"]
print(thislist)
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1


###########
# Method 4: Looping Using List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
###########
thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
print(thislist)
[print(x) for x in thislist]

newlist = [x for x in thislist if "a" in x]
print(newlist)
print()

# Without list comprehension you will have to write a for statement with a conditional test inside.
newlist = []
for x in thislist:
    if "a" in x:
        newlist.append(x)
print(newlist)
print()

newlist = [x for x in range(10) if x < 5]
print(newlist)
print()

newlist = [x.upper() for x in thislist]
print(newlist)
print()

newlist = [x if x != "banana" else "orange" for x in thislist]
# The expression in the example above says:
# "Return the item if it is not banana, if it is banana return orange".
print(newlist)
print()

###########
# Method 5: Using a iterator
###########
thislist = ["apple", "banana", "cherry"]
print(thislist)
myit = iter(thislist)

print(next(myit))
print(next(myit))
print(next(myit))
print()

###########
# Python - Sort Lists
###########
print(">>>Sort List Alphanumerically")
thislist.sort()
print(thislist)


