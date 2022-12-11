#!/usr/bin/python
# -*- coding: UTF-8 -*-

# class　Quick {
#     　public　void　sort(int　arr[],int　low,int　high) {
#         　int　l=low;
#         　int　h=high;
#         　int　povit=arr[low];
#          
#         　while(l<h) {
#             　while(l<h&&arr[h]>=povit)
#             　    h--;
#             　if(l<h){
#                 　arr[l]=arr[h];
#                 　l++;
#             　}
#              
#             　while(l<h&&arr[l]<=povit)
#             　    l++;
#              
#             　if(l<h){
#                 　arr[h]=arr[l];
#                 　h--;
#             　}
#         　}
#             num[l]=povit;
#         　print(arr);
#         　System.out.print("l="+(l+1)+"h="+(h+1)+"povit="+povit+"\n");
#         　if(l-1>low)sort(arr,low,l-1);
#         　if(h+1<high)sort(arr,h+1,high);
#     　}
# }


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


# 示例：
array = [2, 3, 35, 7, 1, 4, 6, 105, 5, 55, 77, 9, 10, 15, 19, 17, 12]
print(quick_sort(array))
