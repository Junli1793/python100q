"""
Python RegEx
https://www.w3schools.com/python/python_regex.asp

A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

The re module offers a set of functions that allows us to search a string for a match:
findall 	Returns a list containing all matches
search 	    Returns a Match object if there is a match anywhere in the string
split 	    Returns a list where the string has been split at each match
sub 	    Replaces one or many matches with a string

"""

###########
# The findall() Function
###########
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
x = re.findall(r"a.n", txt)
print(x)

x = re.findall("Portugal", txt)
print(x)

string = """Hello my Number is 123456789 and
    my friend's number is 987654321"""

regex = r'\d+'
match = re.findall(regex, string)
print(match)

###########
# The search() Function
# If there is more than one match, only the first occurrence of the match will be returned.
###########
x = re.search(r"\s", txt)
print(x)
print("The first white-space character is located in position:", x.start())
print("The first white-space character is located in position:", x.end())
print()

# A Python program to demonstrate working of re.match().
# import re

# Lets use a regular expression to match a date string
# in the form of Month name followed by day number
regex = r"([a-zA-Z]+) (\d+)"

match = re.search(regex, "I was born on June 24")

if match != None:

    # We reach here when the expression "([a-zA-Z]+) (\d+)"
    # matches the date string.

    # This will print [14, 21), since it matches at index 14
    # and ends at 21.
    print("Match at index % s, % s" % (match.start(), match.end()))

    # We us group() method to get all the matches and
    # captured groups. The groups contain the matched values.
    # In particular:
    # match.group(0) always returns the fully matched string
    # match.group(1) match.group(2), ... return the capture
    # groups in order from left to right in the input string
    # match.group() is equivalent to match.group(0)

    # So this will print "June 24"
    print("Full match: % s" % (match.group(0)))

    # So this will print "June"
    print("Month: % s" % (match.group(1)))

    # So this will print "24"
    print("Day: % s" % (match.group(2)))

else:
    print("The regex pattern does not match.")


###########
# The split() Function
# The split() function returns a list where the string has been split at each match.
###########
print()
print(txt)
x = re.split(r"\s", txt)
print(type(x))
print(x)

x = re.split(r"\s", txt, 1)
print(x)

# example 1
print()
from re import split

# '\W+' denotes Non-Alphanumeric Characters
# or group of characters Upon finding ','
# or whitespace ' ', the split(), splits the
# string from that point
print(split(r'\W+', 'Words, words , Words'))
print(split(r'\W+', "Word's words Words"))

# Here ':', ' ' ,',' are not AlphaNumeric thus,
# the point where splitting occurs
print(split(r'\W+', 'On 12th Jan 2016, at 11:02 AM'))

# '\d+' denotes Numeric Characters or group of
# characters Splitting occurs at '12', '2016',
# '11', '02' only
print(split(r'\d+', 'On 12th Jan 2016, at 11:02 AM'))


# example 2
print()
# import re

# Splitting will occurs only once, at
# '12', returned list will have length 2
print(re.split(r'\d+', 'On 12th Jan 2016, at 11:02 AM', 1))

# 'Boy' and 'boy' will be treated same when
# flags = re.IGNORECASE
print(re.split(r'[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))
print(re.split(r'[a-f]+', 'Aey, Boy oh boy, come here'))


###########
# re.sub()
# The ‘sub’ in the function stands for SubString,
# a certain regular expression pattern is searched in the given string(3rd parameter),
# and upon finding the substring pattern is replaced by repl(2nd parameter),
# count checks and maintains the number of times this occurs.
###########
# import re
print()

# Regular Expression pattern 'ub' matches the
# string at "Subject" and "Uber". As the CASE
# has been ignored, using Flag, 'ub' should
# match twice with the string Upon matching,
# 'ub' is replaced by '~*' in "Subject", and
# in "Uber", 'Ub' is replaced.
print(re.sub(r'ub', '~*', 'Subject has Uber booked already',
             flags=re.IGNORECASE))

# Consider the Case Sensitivity, 'Ub' in
# "Uber", will not be replaced.
print(re.sub(r'ub', '~*', 'Subject has Uber booked already'))

# As count has been given value 1, the maximum
# times replacement occurs is 1
print(re.sub(r'ub', '~*', 'Subject has Uber booked already',
             count=1, flags=re.IGNORECASE))

# 'r' before the pattern denotes RE, \s is for
# start and end of a String.
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam',
             flags=re.IGNORECASE))

