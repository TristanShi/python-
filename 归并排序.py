#-*- coding: utf-8 -*-
# O(nlog n) 不稳定
"""即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。"""

def merge_sort(list):
        if len(list) <= 1:
            return list
        num = int(len(list)/2)
        left  = merge_sort(list[:num])
        right = merge_sort(list[num:])
        return merge(left, right)

def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += right[r:]
    result += left[l:]
    return result

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20,55, 34, 30, 45]
print merge_sort(alist)
