#-*- coding: utf-8 -*-
"""一，买书问题 编程之美
#      上柜的《哈利波特》平装本系列，一共有五卷。假设每一卷单独销售均需8欧元。如果读者一次购买不同的两卷，就可以扣除5%的费用，三卷则更多。
# 假设具体折扣的情况如下：
#        本数    2       折扣   5%
#        本数    3       折扣  10%
#        本数    4       折扣  20%
#        本数    5       折扣  25%
# 问题：设计出算法，能够计算出读者所购买的一批书的最低价格。

#利用动态规划,层层递归"""

def min_price(array):            # array必须是由数字组成的数列,且长度为5.
    if len(array) != 5:
        return "Invaild Format"
    array = sorted(array)       # 首先进行从小到大排列,
    if array[0] >= 1:           # 如果最小值array[0]大于等于1的话,那么意味可以买5本不同的书,同时,然后每一位减1后进行递归计算
        return 0.75 * 8 * 5 + min_price(array=[array[0]-1,array[1]-1,array[2]-1,array[3]-1,array[4]-1])
    elif array[1] >= 1:         # 除此之外,如果array[1]大于等于1的话,那么意味可以买4本不同的书,同时,然后后四位每一位减1后进行递归计算
        return 0.8 * 8 * 4 + min_price(array=[array[0],array[1]-1,array[2]-1,array[3]-1,array[4]-1])
    elif array[2] >= 1:
        return 0.9 * 8 * 3 + min_price(array=[array[0],array[1],array[2]-1,array[3]-1,array[4]-1])
    elif array[3] >= 1:
        return 0.95* 8 * 2 + min_price(array=[array[0],array[1],array[2],array[3]-1,array[4]-1])
    elif array[4] >= 1:
        return 8 * 1 + min_price(array=[array[0],array[1],array[2],array[3],array[4]-1])
    elif array[4] == 0:
        return 0                # 最后如果当 array的值都为0的时候,直接返回0,结束递归.


array = [1, 1, 1, 1, 1]
print min_price(array)
