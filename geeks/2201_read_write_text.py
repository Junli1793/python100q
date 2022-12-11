
"""
Reading and Writing to text files in Python
https://www.geeksforgeeks.org/reading-writing-text-files-python/
"""

# Open file does not exist
# file0 = open("myfile0.txt", "r")
# file0 = open("myfile0.txt", "r+")


# Open function to open the file "MyFile1.txt"
# (same directory) in append mode and
file1 = open("myfile1.txt", "a")
file1.write("open with append mode in myfile1.txt\n")
file1.close()

# store its reference in the variable file1
# and "MyFile2.txt" in D:\Text in file2
file2 = open(r"myfile1.txt", "w+")
file2.write("open with w+ mode in myfile1.txt\n")
file2.close()

file3 = open("myfile1.txt", "r+")

print(">>>Output of Read function is:")
print(file3.read())

file3.write("open with r+ mode and write to myfile1.txt\n")
file3.seek(0)
print(">>>Output of Read function after write and seek(0) is:")
print(file3.read())

print()
file3.close()

#########################
# Writing to a file and Reading from a file
#########################

# Program to show various ways to read and
# write data in a file.
file1 = open("myfile2.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes

file1 = open("myfile2.txt", "r+")

print(">>>Output of Read() function in myfile2.txt is: ")
print(file1.read())
# print()

# seek(n) takes the file handle to the nth
# bite from the beginning.
file1.seek(0)

print(">>>Output of Readline() function in myfile2.txt is: ")
print(file1.readline())
# print()

# seek(n) takes the file handle to the nth
# bite from the beginning.
file1.seek(0)

# To show difference between read and readline
print(">>>Output of Read(9) function in myfile2.txt is: ")
print(file1.read(9))
print()

# seek(n) takes the file handle to the nth
# bite from the beginning.
file1.seek(0)

print(">>>Output of Readline(9) function in myfile2.txt is: ")
print(file1.readline(9))

file1.seek(0)
# readlines function
print(">>>Output of Readlines() function in myfile2.txt is: ")
print(file1.readlines())
print()

file1.seek(0)
print(">>>Output of Readlines()[1] function in myfile2.txt is: ")
print(file1.readlines()[1])
print()

file1.close()

###########################
# Appending to a file
###########################

# Python program to illustrate
# Append vs write mode
file1 = open("myfile_a.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.writelines(L)
file1.close()

# Append-adds at last
file1 = open("myfile_a.txt", "a")  # append mode
file1.write("Today \n")
file1.close()

file1 = open("myfile_a.txt", "r")
print(">>>Output of Readlines after appending of myfile_a.txt: ")
print(file1.readlines())
print()
file1.close()

# Write-Overwrites
file1 = open("myfile_a.txt", "w")  # write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open("myfile_a.txt", "r")
print(">>>Output of Readlines after writing of myfile_a.txt: ")
print(file1.readlines())
print()
file1.close()
