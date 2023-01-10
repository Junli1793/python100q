#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Open the file in read mode
with open("data.txt", "r") as file1:
    # Read file into a list
    lines = file1.readlines()

    # Remove duplicated lines
    unique_lines = list(set(lines))

    print(unique_lines)
file1.close()

# Open the file in write mode
file2 = open("data2.txt", "w")
file2.writelines(unique_lines)
file2.close()
