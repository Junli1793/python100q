"""
Reading and Writing XML Files in Python
https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python

Note: In general, the process of reading the data from an XML file and analyzing its logical components is known as Parsing.
Therefore, when we refer to reading a xml file we are referring to parsing the XML document.

For the purpose of reading and writing the xml file we would be using a Python library named BeautifulSoup.
Install:
    pip install beautifulsoup4
    pip install lxml

"""

import requests
from bs4 import BeautifulSoup

print("Fetch the XML by requests and then parse it by BeautifulSoup".center(80, "*"))

# Fetch the XML document
xml_doc = requests.get('http://www.example.com/data.xml').text

# Parse the document using BeautifulSoup
soup = BeautifulSoup(xml_doc, 'xml')

# Find elements in the document using tags and attributes
elements = soup.find_all('item', attrs={'id': '123'})

# Extract data from the elements
for element in elements:
    title = element.find('title').text
    description = element.find('description').text
    print(f'Title: {title}\nDescription: {description}\n')


###########
# Reading Data From an XML File
###########

from bs4 import BeautifulSoup

# Reading the data inside the xml
# file to a variable under the name
# data
with open('dict.xml', 'r') as f:
    data = f.read()

# Passing the stored data inside
# the beautifulsoup parser, storing
# the returned object
Bs_data = BeautifulSoup(data, "xml")

# Finding all instances of tag `root`
b_root = Bs_data.find_all('root')

print("root".center(80, "*"))
print(b_root)

# Using find() to extract attributes of the first instance of the tag
b_name = Bs_data.find('child', {'name': 'Frank'})

print("child".center(80, "*"))
print(b_name)

# Extracting the data stored in a specific attribute of the `child` tag
# value = b_name.get('age')
value = b_name.find('address')

print("address".center(80, "*"))
print(value)


###########
# Writing an XML File
###########

# from bs4 import BeautifulSoup

# Reading data from the xml file
with open('dict.xml', 'r') as f:
    data = f.read()

# Passing the data of the xml
# file to the xml parser of
# beautifulsoup
bs_data = BeautifulSoup(data, 'xml')

# A loop for replacing the value
# of attribute `test` to WHAT !!
# The tag is found by the clause
# `bs_data.find_all('child', {'name':'Frank'})`
for tag in bs_data.find_all('child', {'name':'Frank'}):
    tag['test'] = "WHAT !!"


# Output the contents of the
# modified xml file
print("Writing an XML File".center(80, "*"))
print(bs_data.prettify())
print()
