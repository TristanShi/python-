#-*- coding: utf-8 -*-
# O(nlog n) 不稳定


def heap_sort(lst):
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    # 创建最大堆
    for start in xrange((len(lst) - 2) // 2, -1, -1):
        sift_down(start, len(lst) - 1)

    # 堆排序
    for end in xrange(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)
    return lst

l = [9,2,1,7,6,8,5,3,4]
print heap_sort(l)

##########
def opt_heapsort(s):
    sl = len(s)

    def swap(pi, ci):
        if s[pi] < s[ci]:
            s[pi], s[ci] = s[ci], s[pi]

    def sift(pi, unsorted):
        i_gt = lambda a, b: a if s[a] > s[b] else b
        while pi*2+2 < unsorted:
            gtci = i_gt(pi*2+1, pi*2+2)
            swap(pi, gtci)
            pi = gtci
    # heapify
    for i in range((sl/2)-1, -1, -1):
        sift(i, sl)
    # sort
    for i in range(sl-1, 0, -1):
        swap(i, 0)
        sift(0, i)
