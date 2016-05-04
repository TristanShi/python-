#-*- coding: utf-8 -*-
"""
编程之美:
实现一个函数，输入一个无符号整数，输出该数二进制中的1的个数。例如把9表示成二进制是1001，有2位是1，因此如果输入9，该函数输出2
"""

def count2bin(x):
    '''
    将输入的数字除以2, 余数就是二进制位上的数, 除后的结果继续循环除,知道结果为0.
    e.g. 13  13/2 = 6,1  6/2 = 3,0   3/2 = 1,1  1/2 = 0,1 break output=[1, 0, 1, 1]
    '''
    num = x
    mid = []
    while True:
        if num == 0:
            break
        num, rem = divmod(num, 2)
        mid.append(rem)

    return sum(mid)

def Array2bin():
    '''
    利用二进制计数算出0-255直接所有二进制中1的个数,存储在数列中
    :return:
    '''
    l = []
    for i in xrange(0,256):
        count = count2bin(i)
        l.append(count)
    return l

array2bin = Array2bin()

def count_2bin(x):      # 以存储空间来换时间空间,直接查询
    return array2bin[x]

print count_2bin(201)

