#-*- coding: utf-8 -*-
#O(n^2) 稳定排序
""" 每步将一个待排序的纪录，按其关键码值的大小插入前面已经排序的文件中适当位置上，直到全部插入完为止。"""

def insert_sort(k):
    for i in xrange(1, len(k)):
        j = i
        while j > 0 and k[j] < k[j-1]:   #while 循环将j和小于j的所有进行一次比较
            k[j], k[j-1] = k[j-1], k[j]
            j -= 1
    return k

array = [ 12, 15, 8, 20, 6, 7, 100, 33, 43, 40, 50, 70, 20]
print insert_sort(array)

