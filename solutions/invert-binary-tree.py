#!/usr/bin/env python
# encoding: utf-8

"""
invert-binary-tree.py
 
Created by Shuailong on 2016-02-10.

https://leetcode.com/problems/invert-binary-tree/.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        tmp = root.left
        root.left = root.right
        root.right = tmp
        return root



def main():
    solution = Solution()
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    root = solution.invertTree(root)
    print root.left.val
    
if __name__ == '__main__':
    main()

        