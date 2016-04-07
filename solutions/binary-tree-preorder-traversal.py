#!/usr/bin/env python
# encoding: utf-8

"""
binary-tree-preorder-traversal.py
 
Created by Shuailong on 2016-04-07.

https://leetcode.com/problems/binary-tree-preorder-traversal/.

"""

'''Iterative way: think about it. '''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)        

def main():
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)

    root = t1
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7

    solution = Solution1()
    print solution.preorderTraversal(root)

if __name__ == '__main__':
    main()

        