#!/usr/bin/env python
# encoding: utf-8

"""
same-tree.py
 
Created by Shuailong on 2016-02-10.

https://leetcode.com/problems/same-tree/.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is not None and q is not None:
            if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
            else:
                return False
        else:
            if p is None and q is None:
                return True
            if p is None and q is not None:
                return False
            if p is not None and q is None:
                return False
            

def main():
    pass
    
if __name__ == '__main__':
    main()

