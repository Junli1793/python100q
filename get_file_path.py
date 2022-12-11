#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
from pathlib import Path

# -- Adding wireless library in to path variable
# cwd = Path(__file__).parents[2]
cwd = Path(__file__).parents[0]

device_lib_directory = "{}/device_library".format(cwd)
sys.path.append('{}'.format(device_lib_directory))

print("System path 1:\n {}".format(sys.path))

# print(device_lib_directory)
print("System path 2:\n {}".format(device_lib_directory))

