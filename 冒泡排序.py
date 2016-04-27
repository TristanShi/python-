#-*- coding: utf-8 -*-
# O(n^2）稳定
""" 重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
# 走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。 """

def bubble_sort(k):
    for passnum in range(len(k)-1, 0, -1):
        for j in range(passnum):
            if k[j] > k[j+1]:   #每一次都把最大的数移到了最后一位
                k[j], k[j+1] = k[j+1],k[j]
    return k

array = [12, 15, 8, 20, 6, 7, 100, 33, 43]
bubble_sort(array)
print array

##########
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)