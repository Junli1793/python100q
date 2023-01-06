#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
Python program to create a dict1ionary from a string
https://www.geeksforgeeks.org/python-program-to-create-a-dict1ionary-from-a-string/?ref=lbp

"""

###########
# Method 1-1:  Using eval()
###########

# Python3 code to convert
# a string to a dict1ionary

# Initializing String
import json

string = "{'A':13, 'B':14, 'C':15}"

# eval() convert string to dict1ionary
dict1 = eval(string)
print(dict1)
print(dict1['A'])
print(dict1['C'])

employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
dict1 = eval(employee)
print(dict1)

###########
# Method 1-2:  Using json.loads()
###########

employee_dict1 = json.loads(employee)
print(employee_dict1)

print(employee_dict1['name'])

###########
# Method 2:  Using generator expressions in python
###########

# Python3 code to convert
# a string to a dict1ionary

# Initializing String
string = "A - 13, B - 14, C - 15"

# Converting string to dict1ionary
dict1 = dict((x.strip(), int(y.strip()))
            for x, y in (element.split('-')
                         for element in string.split(', ')))

print(dict1)
print(dict1['A'])
print(dict1['C'])
