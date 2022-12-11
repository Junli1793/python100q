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

print(">>>thisdict.items()")
for x, y in thisdict.items():
    print(x, y)

print()
print(type(thisdict.items()))
print(thisdict.items())
print(list(thisdict.items()))
