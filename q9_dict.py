#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key, value)
    time.sleep(1)  # 暂停 1 秒

myDic = {1: 'aaa', 3: 'ccc'}
for k, v in dict.items(myDic):
    print(k, v)
    time.sleep(1)

    """
    merge 2 dicts
    """
# dic3 = dict(myD.items() + myDic.items())
myD.update(myDic)
for k3, v3 in dict.items(myD):
    print(k3, v3)
    time.sleep(1)

dic4 = dict(myD, **myDic)
for k4, v4 in dict.items(dic4):
    print(k4, v4)
    time.sleep(1)
