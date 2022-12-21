"""
Python - Loop Lists
https://www.w3schools.com/python/python_lists_loop.asp

"""

###########
# Method 1: for loop
# We can also use a for loop to iterate through an iterable object
# (that is either a list, a tuple, a dictionary, a set, or a string).
# The for loop actually creates an iterator object and executes the next() method for each loop.
###########
print(">>>Loop Through by for loop")
thislist = ["apple", "banana", "cherry"]
print(thislist)
for x in thislist:
    print(x)

###########
# Method 2: Loop Through the Index Numbers
###########
print(">>>Loop Through the Index Numbers")
thislist = ["apple", "banana", "cherry"]
print(thislist)
for i in range(len(thislist)):
    print(thislist[i])

###########
# Method 3: Using a While Loop
###########
print(">>>Using a While Loop")
thislist = ["apple", "banana", "cherry"]
print(thislist)
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

###########
# Method 4: Looping Using List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
###########
print(">>>Looping Using List Comprehension")
thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
print(thislist)
[print(x) for x in thislist]

newlist = [x for x in thislist if "a" in x]
print(newlist)
print()

# Without list comprehension you will have to write a for statement with a conditional test inside.
newlist = []
for x in thislist:
    if "a" in x:
        newlist.append(x)
print(newlist)
print()

newlist = [x for x in range(10) if x < 5]
print(newlist)
print()

newlist = [x.upper() for x in thislist]
print(newlist)
print()

newlist = [x if x != "banana" else "orange" for x in thislist]
# The expression in the example above says:
# "Return the item if it is not banana, if it is banana return orange".
print(newlist)
print()

###########
# Method 5: Using a iterator
###########
print(">>>Loop by using a iterator")
thislist = ["apple", "Orange", "Kiwi", "banana", "cherry"]
print(thislist)
myit = iter(thislist)

print(next(myit))
print(next(myit))
print(next(myit))
print()

###########
# Python - Sort Lists
###########
print(">>>Sort List Alphanumerically")
thislist.sort()
print(thislist)

print(">>>Sort Descending")
thislist.sort(reverse=True)
print(thislist)

print(">>>Customize Sort Function")
thislist.sort(key=str.lower)
print(thislist)

print(">>>Reverse Order")
thislist.reverse()
print(thislist)

print(">>>sorted() function")
# sorted(iterable, key=None, reverse=False)
l1 = [5, 2, 3, 1, 4]
print(sorted(l1))
print(l1)

d1 = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
print(sorted(d1))
print(d1)

example_list = [5, 0, 6, 1, 2, 7, 3, 4]
result_list1 = sorted(example_list, key=lambda x: x * -1)
print(result_list1)
print()

result_list2 = sorted(example_list, reverse=True)
print(result_list2)

print()

# 复杂的实例
s = "德国 10 11 16\n意大利 10 10 20\n荷兰 10 12 14\n法国 10 12 11\n英国 22 21 22\n中国 38 32 18\n日本 27 14 17\n美国 39 41 33\n俄罗斯奥委会 20 28 23\n澳大利亚 17 7 22\n匈牙利 6 7 7\n加拿大 7 6 11\n古巴 7 3 5\n巴西 7 6 8\n新西兰 7 6 7"
stodata = s.split('\n', -1)

# 使用sorted
para = {}

for line in range(len(stodata)):
    # 每一行数据
    data = stodata[line].split(' ')
    print(data)
    # 组装数据结构para={'China': [], 'Russia': []}
    para[data[0]] = [int('-' + i) for i in data[1:]]
# 开始排序(x[1]代表奖牌数目, x[0]代表国家)
new_para = sorted(para.items(), key=lambda x: (x[1], x[0]))
print()

c = []
for i in new_para:
    c.append((i[0]))
for j in range(15):
    print(f"{(j + 1):2d}  {c[j]}")
