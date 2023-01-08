"""
Reading and Writing JSON to a File in Python
https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/

The full form of JSON is Javascript Object Notation.
It means that a script (executable) file which is made of text in a programming language, is used to store and transfer the data.
Python supports JSON through a built-in package called JSON.
To use this feature, we import the JSON package in Python script.
The text in JSON is done through quoted-string which contains the value in key-value mapping within { }.
It is similar to the dictionary in Python.
"""

# Writing JSON to a file in Python

"""
Method 1: Writing JSON to a file in Python using json.dumps()

The JSON package in Python has a function called json.dumps() that helps in converting a dictionary to a JSON object. 
It takes two parameters:
    dictionary – the name of a dictionary which should be converted to a JSON object.
    indent – defines the number of units for indentation

After converting the dictionary to a JSON object, simply write it to a file using the “write” function.
"""

import json
from pprint import pformat

print()
print("==============Example 1: json.dumps(dict)==============")

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

# Serializing json
print("json.dumps(dictionary, indent=4)")
json_object = json.dumps(dictionary, indent=4)
print(type(json_object))
print(json_object)
print()

# Writing to sample.json
with open("myjson_1.json", "w") as outfile:
    outfile.write(json_object)

print()
print("==============Example 1: json.loads(json_str)==============")

dict1 = json.loads(json_object)
print("json.loads(json_object)")
print(type(dict1))
print(dict1)
print()

"""
Method 2: Writing JSON to a file in Python using json.dump()

Another way of writing JSON to a file is by using json.dump() method The JSON package has the “dump” function which directly writes the dictionary to a file in the form of JSON, 
without needing to convert it into an actual JSON object. It takes 2 parameters:
    dictionary – the name of a dictionary which should be converted to a JSON object.
    file pointer – pointer of the file opened in write or append mode.
"""
# import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

print()
print("==============Example 2: json.dump(dict)==============")

print("json.dump(dictionary, outfile)")
print(type(dictionary))
print(dictionary)
print()

with open("myjson_2.json", "w") as outfile:
    json.dump(dictionary, outfile)

"""
Reading JSON from a file using  json.load()

The JSON package has json.load() function that loads the JSON content from a JSON file into a dictionary. 
It takes one parameter:
    File pointer: A file pointer that points to a JSON file.
"""
# import json

print()
print("==============Example 2: json.load(json_file)==============")

# Opening JSON file
with open('myjson_1.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print("json.load(openfile)")
print(json_object)
print(type(json_object))
print(pformat(json_object))
print()

"""
json.loads()

json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary. 
It is mainly used for deserializing native string, byte, or byte array which consists of JSON data into Python Dictionary.
"""

# import json

# JSON string:
# Multi-line string
data = """{
	"Name": "Jennifer Smith",
	"Contact Number": 7867567898,
	"Email": "jen123@gmail.com",
	"Hobbies":["Reading", "Sketching", "Horse Riding"]
	}"""

print()
print("==============Example 3: json.loads(json_str)==============")

# parse data:
print(type(data))
print(data)
print()
dict2 = json.loads(data)

print("json.loads(data)")
# the result is a Python dictionary:
print(type(dict2))
print(dict2)
print(pformat(dict2))
print()

"""
Append to JSON file using Python
https://www.geeksforgeeks.org/append-to-json-file-using-python/

"""

###########
# Example 1: Updating a JSON string.
###########

import json

print()
print("==============Example 4: Updating a JSON string((json.dumps(dict)))==============")

# JSON data:
x = """{ "organization":"GeeksForGeeks",
"city":"Noida",
"country":"India"}"""

# python object to be appended
y = {"pin": 110096}
print(type(y))

# parsing JSON string:
z = json.loads(x)
print(type(z))

# appending the data
z.update(y)

s = json.dumps(z)
print(type(s))
# the result is a JSON string:
print(s)

###########
# Example 2: Updating a JSON file.
###########

import json

print()
print("==============Example 5: function to add to JSON (json.dump(dict))==============")

# function to add to JSON
def write_json(new_data, filename='myjson_3.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)

        emp_count = len(file_data["emp_details"]) + 1
        new_data["emp_name"] = new_data["emp_name"] + str(emp_count)

        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)

        # Sets file's current position at offset.
        file.seek(0)

        # convert back to json.
        json.dump(file_data, file, indent=4)
        print(file_data)


# python object to be appended
y = {"emp_name": "Nikhil",
     "email": "nikhil3@geeksforgeeks.org",
     "job_profile": "Full Time"
     }

write_json(y)
