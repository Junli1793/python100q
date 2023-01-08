"""
Reading and Writing CSV Files in Python
https://www.geeksforgeeks.org/reading-and-writing-csv-files-in-python/
"""

#########################
# Python program to demonstrate
# writing to CSV
#########################

import csv

print()
print("==============Example 1: csv.writer(csvfile)==============")

# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

# name of csv file
filename = "mycsv.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)

#########################
# Writing a dictionary to a CSV file
#########################
# importing the csv module
import csv

print()
print("==============Example 2: csv.DictWriter(csvfile, fieldnames=fields)==============")

# my data rows as dictionary objects
mydict = [{'branch': 'COE', 'cgpa': '9.0',
           'name': 'Nikhil', 'year': '2'},
          {'branch': 'COE', 'cgpa': '9.1',
           'name': 'Sanchit', 'year': '2'},
          {'branch': 'IT', 'cgpa': '9.3',
           'name': 'Aditya', 'year': '2'},
          {'branch': 'SE', 'cgpa': '9.5',
           'name': 'Sagar', 'year': '1'},
          {'branch': 'MCE', 'cgpa': '7.8',
           'name': 'Prateek', 'year': '3'},
          {'branch': 'EP', 'cgpa': '9.1',
           'name': 'Sahil', 'year': '2'}]

# field names
fields = ['name', 'branch', 'year', 'cgpa']

# name of csv file
filename = "mycsv_1.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(mydict)

#########################
# Python program to demonstrate
# reading from CSV
#########################

print()
print("==============Example 3: csv.reader(csvfile)==============")

with open('mycsv.csv', mode='r') as csvfile:
    print(">>>reading mycsv.csv")
    # reading the CSV file
    print(">>>csv.reader(file)")
    csvreader = csv.reader(csvfile)

    # iterator
    print(type(csvreader))
    print(csvreader.__iter__().__next__())
    print()

    # displaying the contents of the CSV file
    for lines in csvreader:
        print(lines)

    print(">>>csv.DictReader(file)")
    csvfile.seek(0)
    list_csv_dicreader = list(csv.DictReader(csvfile))
    print(list_csv_dicreader)

    i = 0
    for line in list_csv_dicreader:
        i += 1
        print(f">>>line_{i}")
        print(line)

    """
    An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
    Technically, in Python, an iterator is an object which implements the iterator protocol, 
    which consist of the methods __iter__() and __next__().
    
    Lists, tuples, dictionaries, and sets are all iterable objects. 
    They are iterable containers which you can get an iterator from.
    All these objects have a iter() method which is used to get an iterator.
    """
    i = 0
    for line in list_csv_dicreader:
        i += 1
        print(f">>>line_{i}")
        print(type(line))   # <class 'collections.OrderedDict'>
        print(line)
        print(">>> get first item of line(OrderedDict) by its iterator by next(iter(line.items()))")
        it = iter(line.items())
        print(next(it))
        print(">>> get second item of line(OrderedDict) by its iterator by next(iter(line.items()))")
        print(next(it))
        print(">>> get third item of line(OrderedDict) by its iterator by next(iter(line.items()))")
        print(next(it))
        print()

        j = 0
        for item in line.items():
            j += 1
            print(f"    >>>tuple_{j}:{item}")
            print(f"    key:{item[0]}")
            print(f"    value:{item[1]}")

        for key, value in line.items():
            print(f"{key}: {value}")

        print(type(line.items()))
        print(line.items())
        print(list(line.items()))
