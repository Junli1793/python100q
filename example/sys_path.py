#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
Sys is a built-in Python module that contains parameters specific to the system i.e. it contains variables and methods that interact with the interpreter and are also governed by it.

sys.path

sys.path is a built-in variable within the sys module. It contains a list of directories that the interpreter will search in for the required module.

When a module(a module is a python file) is imported within a Python file, the interpreter first searches for the specified module among its built-in modules.
If not found it looks through the list of directories(a directory is a folder that contains related modules) defined by sys.path.

"""

import sys
from pathlib import Path

print()
print("==============Example 1==============")
cwd = Path(__file__).parents[0]
print(cwd)

pd = Path(__file__).parents[1]
print(pd)

gd = Path(__file__).parents[2]
print(gd)

print()
print("==============Example 2==============")

device_lib_directory = "{}/device_library".format(cwd)
sys.path.append('{}'.format(device_lib_directory))

print("System path 1:\n {}".format(sys.path))

print()
print("==============Example 3==============")

print("System path 2:\n {}".format(device_lib_directory))

print()
print("==============Example 4==============")

if len(sys.argv) == 2:
    path = sys.argv[1]
print(f"path from command line: {path}")

print()
print("==============Example 5==============")

print("exit the interpreter:\n")
# sys.exit()
sys.exit(1)
