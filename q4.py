#!/usr/bin/python
# -*- coding: UTF-8 -*-

year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 1 < month < 12 :
    sumd = months[month - 1] 
else:
    print('data error')
sumd += day
leap = 0
if(year % 400 == 0) or (year % 4 == 0) or (year % 100 != 0):
    leap = 1
if (leap == 1) and month > 2:
    sumd += 1
print('it is the %dth day.' % sumd)
