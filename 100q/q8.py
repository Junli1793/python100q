#!/usr/bin/python3
# -*- coding: UTF-8 -*-

for i in range(1, 10):
    print()
    for j in range(1, i + 1):
        print("%dx%d=%d " % (i, j, i * j), end='')
