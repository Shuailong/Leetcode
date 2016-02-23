#!/usr/bin/env python
# encoding: utf-8

"""
closest-binary-search-tree-value.py
 
Created by Shuailong on 2016-02-18.

https://leetcode.com/problems/closest-binary-search-tree-value/.

"""

'''Not solved yet'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """

        if root is not None:
            diff = root.val-target
        else:
            return float('inf')

        if target == root.val:
            return root.val
        elif target < root.val:
            next_diff = self.closestValue(root.left, target) - target
            if abs(diff) > abs(next_diff):
                return int(next_diff + target)
            else:
                return root.val
        else:
            next_diff = self.closestValue(root.right, target) - target
            if abs(diff) > abs(next_diff):
                return int(next_diff + target)
            else:
                return root.val
        

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
    target = 3.8
    print solution.closestValue(root, target)

if __name__ == '__main__':
    main()

        