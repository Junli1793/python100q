#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''示例1: 使用语法糖@来装饰函数，相当于“myfunc = deco(myfunc)”
但发现新函数只在第一次被调用，且原函数多调用了一次''' 


def deco(func):
    print("before myfunc() called.")
    func()
    print("after myfunc() called.")
    return func


@deco 
def myfunc(): 
    print(" myfunc() called.") 

# myfunc = deco(myfunc)


# print(myfunc)
myfunc() 
myfunc()

'''
output:
before myfunc() called.
 myfunc() called.
after myfunc() called.
 myfunc() called.
 myfunc() called.
 
 这里@deco这一句，和myfunc = deco(myfunc)其实是完全等价的，只不过是换了一种写法而已
一定要记住上面这句！！！！
好了，从现在开始，只需要做替换操作就可以了。
将@deco 替换为 myfunc = deco(myfunc)
程序首先调用deco(myfunc)，得到的返回结果赋值给了myfunc （注意：在Python中函数名只是个指向函数首地址的函数指针而已）
而deco(myfunc)的返回值就是函数myfunc()的地址
这样其实myfunc 没有变化，也就是说，最后的两次myfunc()函数调用，其实都没有执行到deco()。
有同学就问了，明明打印了deco()函数里面的内容啊，怎么说没有调用到呢。
这位同学一看就是没有注意听讲，那一次打印是在@deco 这一句被执行的。
大家亲自动手试一下就会发现” myfunc() called.” 这句打印输出了三次。
多的那次就是@deco这里输出的，因为@deco 等价于myfunc = deco(myfunc)，这里已经调用了deco()函数了。

'''
