"""
Python Dates
https://www.w3schools.com/python/python_datetime.asp

A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
"""

import datetime

x = datetime.datetime.now()
print(">>>datetime.datetime.now()")
print(x)
print(type(x))

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%Y"))
print(x.strftime("%y"))

str1 = x.strftime("%Y_%m_%d_%H_%M_%S")
print(str1)

print(x.strftime("%a"))
print(x.strftime("%A"))
print(x.strftime("%w"))

print(x.strftime("%f"))

# Creating Date Objects
x = datetime.datetime(2020, 8, 8, 23, 22, 21)
print(x)
print()

###########
# time
###########

import time
y = time.time()
print(">>>time.time()")
print(type(y))
print(y)

time.sleep(2)

print(">>>Local time")
str2 = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(y))
print(str2)

print(">>>Local current time")
str3 = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
print(str3)

print(">>>UTC time")
str4 = time.strftime("%Y-%m-%d %H-%M-%S", time.gmtime())
print(str4)

