#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os, sys


path = '../'

print()
print("==============Example 1==============")

files = os.listdir(path)
for name in files:
    print(name)

print()
print("==============Example 2: To get the current working directory==============")

cwd_path1 = os.getcwd()
print(cwd_path1)

print()
print("==============Example 2: To get the full path to the directory a Python file is contained in==============")

full_path = os.path.realpath(__file__)
print("full path: ", full_path)

cwd_path2 = os.path.dirname(full_path)
print("directory: ", cwd_path2)

path, filename = os.path.split(full_path)
print("directory: ", path)
print("file name: ", filename)

print()
print("==============Example 3==============")

for name in files:
    print(cwd_path2 + os.path.sep + name)

print()
print("==============Example 4==============")

files = os.listdir(path)
for name in files:
    print(name)
    full_path = os.path.join(path, name)
    print(full_path)
    file_info = os.stat(full_path)
    print('  ' + str(file_info.st_size))
    print('  ' + str(file_info.st_mode))
    # print('  ' + ('f' if file_info.st_mode & 0O0100000 else '-'))
    # print('  ' + ('d' if file_info.st_mode & 0O0040000 else '-'))
    print()

print()
print("==============Example 5: os method (chdir, mkdir, chmod, rmdir, popen)==============")

import subprocess

os.chdir("../")
os.mkdir("test")
os.chmod("test", 755)

subprocess.Popen(["ls", "-l"])

p = os.popen("ls -l")
print(p.read())
p.close()

os.rmdir("test")

