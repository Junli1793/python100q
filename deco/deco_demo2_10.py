#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
 带参数的装饰器

来想想这个问题，难道@wraps不也是个装饰器吗？
但是，它接收一个参数，就像任何普通的函数能做的那样。
那么，为什么我们不也那样做呢？ 
这是因为，当你使用@my_decorator语法时，你是在应用一个以单个函数作为参数的一个包裹函数。
记住，Python里每个东西都是一个对象，而且这包括函数！
记住了这些，我们可以编写一下能返回一个包裹函数的函数。

在函数中嵌入装饰器

我们回到日志的例子，并创建一个包裹函数，能让我们指定一个用于输出的日志文件。
'''

from functools import wraps

 
def logit(logfile='out.log'):

    def logging_decorator(func):

        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator

 
@logit()
def myfunc1():
    pass

 
myfunc1()
# Output: myfunc1 was called
# 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串

 
@logit(logfile='func2.log')
def myfunc2():
    pass

 
myfunc2()
# Output: myfunc2 was called
# 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串

