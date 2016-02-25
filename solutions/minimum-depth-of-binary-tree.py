#!/usr/bin/env python
# encoding: utf-8

"""
minimum-depth-of-binary-tree.py
 
Created by Shuailong on 2016-02-25.

https://leetcode.com/problems/minimum-depth-of-binary-tree/.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

        

def main():

    n1 = TreeNode(6)
    n2 = TreeNode(4)
    n3 = TreeNode(10)
    n4 = TreeNode(1)
    n5 = TreeNode(7)
    n6 = TreeNode(100)
    n7 = TreeNode(80)
    n8 = TreeNode(30)

    root = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n3.left = n5
    n3.right = n6
    n6.left = n7
    n7.left = n8

    solution = Solution()
    print solution.minDepth(root)
    
if __name__ == '__main__':
    main()

        