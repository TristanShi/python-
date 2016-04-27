#-*- coding: utf-8 -*-
"""#输入一个整形数组, 数组里有正数也有负数. 数组中连续的一个或多个整数组成一个子数组,
#  每个子数组都有一个和. 求所有子数组的和的最大值.
"""

# n ^ 2
def maxS(array):
    max = 0
    low = high = 0      # low表示起始索引值, high表示结束索引值.
    for i in xrange(0, len(array)-1):
        sum = 0         # 每次j的循环结束,设置sum=0
        for j in xrange(i, len(array)):  # sum值从array[i]开始加起
            sum += array[j]
            if sum > max:
                max  = sum
                low  = i
                high = j
    return (low, high, max)


array = [1, -2, -3, 4, -5, -3]
print maxS(array)

# n
# 从头遍历数组元素, 并累加求和, 如果和小于0就自当前元素从新开始, 否则就一直累加, 取其中最大值便为解.

def max_sub_array(array):
    max_end = max_num = array[0]
    high_index = low_index = 0
    for i in xrange(1, len(array)):
        if max_end < 0:                 # 当max_end小于0的时候,直接设置其为array[i].
            max_end = array[i]
            t_low = i                   # 同时设置一个临时的起始索引值为i
        else:
            max_end += array[i]
        if max_end > max_num:
            max_num = max_end
            low_index, high_index = t_low, i
    return (low_index, high_index, max_num)


array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print max_sub_array(array)


# n
def max_sub_array(array):
    max_end = max_num = array[0]
    for i in xrange(1, len(array)):
        max_end = max(array[i], max_end + array[i])
        max_num = max(max_num, max_end)
    return (max_num)


array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print max_sub_array(array)