#!/usr/bin/env python
# encoding: utf-8

"""
binary-search-tree-iterator.py

Created by Shuailong on 2016-05-17.

https://leetcode.com/problems/binary-search-tree-iterator/.

"""


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.inorder = self.visit(root)
        self.p = 0

    def visit(self, root):
        if root is None:
            return []
        return self.visit(root.left) + [root.val] + self.visit(root.right)

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.p < len(self.inorder):
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        res = self.inorder[self.p]
        self.p += 1
        return res


def main():
    t1 = TreeNode(4)
    t2 = TreeNode(2)
    t3 = TreeNode(6)
    t4 = TreeNode(1)
    t5 = TreeNode(3)
    t6 = TreeNode(5)
    t7 = TreeNode(7)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    root = t1

    i, v = BSTIterator(root), []
    while i.hasNext():
        v.append(i.next())
    print v


if __name__ == '__main__':
    main()
