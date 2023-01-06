#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
Python3 List sort()方法
https://www.runoob.com/python3/python3-att-list-sort.html

sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。

sort()方法语法：
list.sort( key=None, reverse=False)

参数
    key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。

返回值
    该方法没有返回值，但是会对列表的对象进行排序。

"""

print()
print("==============Example 1: list1.sort()==============")

thislist = ["apple", "Orange", "Kiwi", "banana", "cherry"]

###########
# Python - Sort Lists
###########
print(">>>Sort List Alphanumerically")
thislist.sort()
print(thislist)

print(">>>reverse=True")
thislist.sort(reverse=True)
print(thislist)

print(">>>sort with key function")
thislist.sort(key=str.lower)
print(thislist)

print(">>>list1.reverse()")
thislist.reverse()
print(thislist)

print()
print("==============Example 2: sorted() function==============")
print("默认为升序")
# sorted(iterable, key=None, reverse=False)
l1 = [5, 2, 3, 1, 4]
print(sorted(l1))
print()

print("原列表不变")
print(l1)
print()

print("sorted() with key function")
example_list = [5, 0, 6, 1, 2, 7, 3, 4]
result_list1 = sorted(example_list, key=lambda x: x * -1)
print(result_list1)
print()

print("reverse=True")
result_list2 = sorted(example_list, reverse=True)
print(result_list2)

print()
print("==============Example 3: sort list of dictionary==============")
list3 = [{"age": 20, "name": "a"}, {"age": 25, "name": "b"}, {"age": 10, "name": "c"}]
list_sorted = sorted(list3, key=lambda x: x["age"])
print(list_sorted)

print()
print("==============Example 4: sort with 2 keys==============")
print("先按照成绩降序排序，相同成绩的按照名字升序排序")
list4 = [{'name': 'alice', 'score': 38}, {'name': 'bob', 'score': 18}, {'name': 'darl', 'score': 28},
         {'name': 'christ', 'score': 28}]
list_sorted = sorted(list4, key=lambda x: (-x['score'], x['name']))
print(list_sorted)

print()
print("==============Example 5: 字符串排序==============")

list5 = ["delphi", "Delphi", "python", "Python", "c++", "C++", "c", "C", "golang", "Golang"]
list5.sort(key=lambda ele: len(ele))  # 按元素长度顺序升序排列
print("升序:", list5)

list5.sort(key=lambda ele: len(ele), reverse=True)  # 按降序排列
print("降序:", list5)

print()
print("==============Example 6: 数值型排序==============")

list6 = [30, 40, 10, 50, 50.1, 80, 60, 100, 90]
list6.sort()
print("升序:", list6)

list6.sort(reverse=True)
print("降序:", list6)

print()
print("==============Example 7: 根据列表中类对象的属性排序==============")


class element(object):
    def __init__(self, id="", name=""):
        self.id = id
        self.name = name

    def __lt__(self, other):  # override <操作符
        print("由于 list.sort() 函数在排序时，使用的是小于号对比，所以自定义的数据类型需要 override __lt__(小于) 函数才能实现排序。")
        if self.id < other.id:
            return True
        return False

    def __str__(self):  # override __str__
        return "id={0},name={1}".format(self.id, self.name)


def sort_by_attribute():
    list7 = [element(id="130", name="json"),
             element(id="01", name="jack"), element(id="120", name="tom")]
    list7.sort()
    for item in list7:
        print(item)


print("根据 element 的 id 属性排序")
sort_by_attribute()

print()
print("==============Example 8: 根据列表中元素的长度排序==============")

list8 = ["delphi", "Delphi", "python", "Python", "c++", "C++", "c", "C", "golang", "Golang"]
list8.sort(key=lambda ele: len(ele))  # 按元素长度顺序升序排列
print("升序:", list8)

list8.sort(key=lambda ele: len(ele), reverse=True)  # 按降序排列
print("降序:", list8)

print("先按字符串长度升序排序，长度相同按字典序升序排序")
list8.sort(key=lambda x: (len(x), x))
print(list8)

print("先按字符串长度升序排序，长度相同按字典序降序排序")
list8.sort(key=lambda x: (len(x), list(map(lambda c: -ord(c), x))))
print(list8)

print("先按字符串长度降序排序，长度相同按字典序升序排序")
list8.sort(key=lambda x: (-len(x), x))
print(list8)

print()
print("==============Example 9: 根据列表中元素的多个属性进行排序==============")

list9 = [["1", "c", "apple"],
         ["2", "c++", "cisco"],
         ["3", "java", "google"],
         ["6", "golang", "google"],
         ["4", "python", "google"],
         ["5", "swift", "apple"]
         ]
list9.sort(key=lambda ele: ele[0])
print("根据第1个元素排序")
print(list9)

list9.sort(key=lambda ele: ele[1])
print("先根据第2个元素排序")
print(list9)

list9.sort(key=lambda ele: (ele[2], ele[1]))
print("先根据第3个元素排序，再根据第2个元素排序")
print(list9)

print()
print("==============Example 10: 动态的根据用户指定的索引进行排序==============")

"""
有时候，在写代码之前，并不知道根据二维表的哪几列排序，而是在程序运行的时候根据输入或配置决定的，
为了解决这个动态根据多个列或属性排序的问题，借助了 eval() 函数，eval() 函数能够把字符串编译成 python 代码并运行，
从而达到动态根据多个列或属性排序的目的。

"""


def two_d_list_sort2(sort_index="0,1,2"):
    list10 = [["1", "c", "apple"],
              ["2", "c++", "cisco"],
              ["3", "java", "google"],
              ["6", "golang", "google"],
              ["4", "python", "google"],
              ["5", "swift", "apple"]
              ]
    key_set = ""
    for item in sort_index.split(","):
        key_set += "ele[" + item + "]+"
    key_set = key_set.rstrip("+")
    list10.sort(key=lambda ele: eval(key_set))
    print("排序索引:", sort_index, "\n", list10)


if __name__ == "__main__":
    print("动态的根据传入的元素索引进行排序")
    two_d_list_sort2("0")
    two_d_list_sort2("1")
    two_d_list_sort2("2")
    two_d_list_sort2("1,0")

print()
print("==============Example 11: 如果非要将列表里不同类型相比较==============")
l11 = [-1, -3, 1, 0, 3, 'a', 'b', 'c']
l11.sort(key=str)
print(l11)

l11.sort()
