#!/usr/bin/env python
# encoding: utf-8

"""
maximum-depth-of-binary-tree.py
 
Created by Shuailong on 2016-02-04.

https://leetcode.com/problems/maximum-depth-of-binary-tree/.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

        

def main():
    solution = Solution()
    root = TreeNode(1)

    print solution.maxDepth(root)
    
if __name__ == '__main__':
    main()

        