"""
Python program to create a dictionary from a string
https://www.geeksforgeeks.org/python-program-to-create-a-dictionary-from-a-string/?ref=lbp

"""

###########
# Method 1-1:  Using eval()
###########

# Python3 code to convert
# a string to a dictionary

# Initializing String
import json

string = "{'A':13, 'B':14, 'C':15}"

# eval() convert string to dictionary
Dict = eval(string)
print(Dict)
print(Dict['A'])
print(Dict['C'])

employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
Dict = eval(employee)
print(Dict)

###########
# Method 1-2:  Using json.loads()
###########

employee_dict = json.loads(employee)
print(employee_dict)

print(employee_dict['name'])

###########
# Method 2:  Using generator expressions in python
###########

# Python3 code to convert
# a string to a dictionary

# Initializing String
string = "A - 13, B - 14, C - 15"

# Converting string to dictionary
Dict = dict((x.strip(), int(y.strip()))
            for x, y in (element.split('-')
                         for element in string.split(', ')))

print(Dict)
print(Dict['A'])
print(Dict['C'])
