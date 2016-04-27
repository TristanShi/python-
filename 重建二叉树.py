#-*- coding: utf-8 -*-
#!/usr/bin/python
#Filename: BTreeNode.py


class BTree():      # Represent a no in a binary tree.
    def __init__(self, c='/0', l=None, r=None): # 定义一个二叉树
        self.e = c
        self.left = l
        self.right = r

def pre_order(bt):  # 前序遍历
    if bt:
        return "%s%s%s" %(bt.e, pre_order(bt.left), pre_order(bt.right))
    return ''

def in_oder(bt):  # 中序遍历
    if bt:
        return "%s%s%s" %(in_oder(bt.left), bt.e, in_oder(bt.right))
    return ''

def post_order(bt):   # 后序遍历
    if bt:
        return "%s%s%s" %(post_order(bt.left), post_order(bt.right), bt.e)
    return ''

def printBTree(bt, depth):
    '''''
       递归打印这棵二叉树，*号表示该节点为NULL
       '''
    '''''
    if not bt:
        ch = '*'
    else:
        ch = bt.e
    '''
    # ch=(lambda x: (x and x.e) or '*')(bt)
    ch = bt.e if bt else '*'
    if depth > 0:
        print "%s%s%s" %((depth-1)*'  ', '--', ch)
    else:
        print ch       # 深度为0的时候,返回ch值, 即为树的根节点
    if not bt:
        return
    printBTree(bt.left, depth+1)  # 递归先打印左边子树, 后打印右边子树.
    printBTree(bt.right, depth+1)


def bulidBTreeFromPreIn(preo, ino):         # preo为前序遍历得到的结果, ino为中序遍历得到的结果
    '''''
    根据前序和中序遍历结果重构这棵二叉树
    '''
    if preo == '' or ino == '':
        return None
    pos = ino.find(preo[0])     # if not find, return -1
    if pos < 0:
        return None
    return BTree(preo[0], bulidBTreeFromPreIn(preo[1:pos+1], ino[0:pos]), bulidBTreeFromPreIn(preo[pos+1:], ino[pos+1:]))

def bulidBTreeFromInPost(ino, posto):       # posto为后序遍历的得到的结果
    '''''
     根据中序和后序遍历结果重构这棵二叉树
     '''
    if ino == '' or posto == '':
        return None
    pos = ino.find(posto[-1])
    if pos < 0:
        return None
    return BTree(posto[-1], bulidBTreeFromInPost(ino[0:pos], posto[0:pos]), bulidBTreeFromInPost(ino[pos+1:], posto[pos:-1]))




if __name__ == '__main__':
    preo = '12473568'
    ino =  '47215386'
    bt = bulidBTreeFromPreIn(preo, ino)
    print "bulid from preorder and inorder"
    print "Preoder is %s" %(pre_order(bt))
    print "Inorder is %s" %(in_oder(bt))
    print "Postorder is %s" %(post_order(bt))
    print "The BTree is:"
    printBTreem(bt, 0)

