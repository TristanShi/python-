##-*- coding: utf-8 -*-
# O(n^2）不稳定
""" 它的工作原理是每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完。"""

def selection_sort(k):
    for i in range(len(k)):
        minN = min(k[i:])
        minNindex = k[i:].index(minN)
        k[i + minNindex], k[i] = k[i], minN   #i+min_index means the initial index of the min
    return k

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20,55, 34, 30, 45]
print selection_sort(alist)

