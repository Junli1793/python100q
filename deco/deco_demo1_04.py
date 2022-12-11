#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''示例7: 在示例4的基础上，让装饰器带参数，
和上一示例相比在外层多了一层包装。
装饰函数名实际上应更有意义些'''


def deco(arg): 

    def _deco(func): 

        def __deco(): 
            print("before %s called [%s]." % (func.__name__, arg)) 
            func() 
            print("after %s called [%s]." % (func.__name__, arg)) 

        return __deco 

    return _deco 


@deco("mymodule") 
def myfunc(): 
    print(" myfunc() called.") 

    
@deco("module2") 
def myfunc2(): 
    print(" myfunc2() called.") 

        
myfunc()
myfunc2()

'''
output:
before myfunc called [mymodule].
 myfunc() called.
after myfunc called [mymodule].
before myfunc2 called [module2].
 myfunc2() called.
after myfunc2 called [module2].

这种带参数的装饰器怎么解释呢。其实是一样的，还是我们的替换操作
@deco(“mymodule”)替换为myfunc = deco(“mymodule”)(myfunc )
注意啊，这里deco后面跟了两个括号。
有同学要问了，这是什么意思？
其实很简单，先执行deco(“mymodule”)，返回结果为_deco
再执行_deco(myfunc)，得到的返回结果为__deco
所以myfunc = __deco

'''
