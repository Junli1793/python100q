#!/usr/bin/python
# -*- coding: UTF-8 -*-


def quick_sort(data):
    """快速排序"""
    if len(data) >= 2:  # 递归入口及出口        
        mid = data[len(data) // 2]  # 选取基准值，也可以选取第一个或最后一个元素        
        left, right = [], []  # 定义基准值左右两侧的列表        
        data.remove(mid)  # 从原始数组中移除基准值        
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data



def q_sort(data):
    if len(data) >= 2:  # 递归入口及出口
        print(data)
        mid = data[len(data)//2]
        left, right = [], []
        data.remove(mid)
        for num in data:
            if num > mid:
                right.append(num)
            else:
                left.append(num)

        return q_sort(left) + [mid] + q_sort(right)
        # ll = q_sort(left)
        # ll.append(mid)
        # ll.extend(q_sort(right))
        # return ll
    else:
        return data

list_of_number = [2, 3, 35, 7, 13, 1, 4, 6, 108, 110, 5, 55, 77, 9, 66, 10, 15, 19, 17, 12]
# print(quick_sort(list_of_number))
print(q_sort(list_of_number))