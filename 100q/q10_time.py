#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import time
import datetime

"""
    python中时间日期格式化符号：
    ------------------------------------
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称  # 乱码
    %% %号本身
"""
print("1, 本地时间为 :", time.localtime())
print(type(time.localtime()))


print("2, time.strftime:")
print(time.strftime('2-1, %Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# 暂停一秒
time.sleep(1)
print(time.strftime('2-2, %Y-%m-%d %H:%M:%S', time.localtime()))
print(time.strftime("2-3, %y/%m/%d %H-%M-%S", time.localtime()))


print("3, 返回当前时间的时间戳（1970纪元后经过的浮点秒数）: ", time.time())
print(type(time.time()))


print(f"4-1, 返回系统运行时间: {time.perf_counter()}")
print(f"4-2, 返回进程运行时间: {time.process_time()}")

print("5, time.mktime 接受时间元组并返回时间戳 :", time.mktime( time.localtime()))


struct_time = time.strptime("30 Nov 00", "%d %b %y")
print("6, time.strptime 返回元组:", struct_time)
print(type(struct_time))


print("7, 用datetime:")
date_time = datetime.datetime.now()
print(type(date_time))
print(date_time.strftime("%Y.%m.%d %H-%M-%S"))
