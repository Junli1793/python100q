#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 将函数作为参数传给另一个函数
def hi():
    return "hi yasoob!"

 
def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())

 
doSomethingBeforeHi(hi)
# outputs:I am doing some boring work before executing hi()
#        hi yasoob!

