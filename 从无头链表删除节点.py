#-*- coding: utf-8 -*-

class Node:
    '''
    建立带指针方向的链表节点
    '''
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class circleList:
    '''
    建立循环链表/无头链表
    '''
    def __init__(self, value, nextNode=None):
        head = self
        self.value = value
        self.nextNode = nextNode
        while True:
            if self.nextNode:
                self = self.nextNode
            else:
                self.nextNode = head
                break

    def remove(self, value):
        '''
        从无头链表删除节点
        '''
        while True:
            if self.value != value:         # 判断节点的值是否等于输入的value,如果否则迭代为下一节点,知道结果为是
                self = self.nextNode
            else:
                self.value = self.nextNode.value        # 将要删除节点的值设为下一节点的值
                self.nextNode = self.nextNode.nextNode  # 将节点指针指向下下个节点
                break                                   # 跳出循环
        return self                                     # 记着下次千万不要忘记写返回值



print circleList(1, Node(2, Node(3, Node(4)))).remove(3).nextNode.nextNode.nextNode.nextNode.value
















