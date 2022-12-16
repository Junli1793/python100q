# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


def twoSum(nums, target):
    index1 = 0
    index2 = 0
    gotit = 0
    # print(len(nums))
    # print(target)
    for i in range(len(nums)):
        print(i)
        index1 = i
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                index2 = j
                gotit = 1
                print(j)
                break
        if gotit == 1:
            break
    return [index1, index2]


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
