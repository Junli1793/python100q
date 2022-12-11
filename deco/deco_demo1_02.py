#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''示例2: 使用内嵌包装函数来确保每次新函数都被调用，
内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''


def deco(func): 

    def _deco(): 
        print("before myfunc() called.") 
        func() 
        print("after myfunc() called.")  
            # 不需要返回func，实际上应返回原函数的返回值 

    return _deco 

    
@deco 
def myfunc(): 
    print(" myfunc() called.") 
    return 'ok'

# myfunc = deco(myfunc)


# print(myfunc)
myfunc() 
myfunc()

'''
output:
before myfunc() called.
 myfunc() called.
after myfunc() called.
before myfunc() called.
 myfunc() called.
after myfunc() called.
 
 @deco 替换为 myfunc = deco(myfunc)
程序首先调用deco(myfunc)，得到的返回结果赋值给了myfunc ，这样myfunc 就变成了指向函数_deco()的指针
以后的myfunc()，其实是调用_deco()
'''
