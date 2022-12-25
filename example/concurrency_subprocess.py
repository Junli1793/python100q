#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""

"""
import subprocess

print()
print("==============Example 1==============")

subprocess.run(["ls", "-l"])  # doesn't capture output

subprocess.run(["ls", "-l", "/usr/"], capture_output=True)

subprocess.run("exit 1", shell=True, check=True)

