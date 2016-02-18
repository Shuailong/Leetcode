#!/usr/bin/env python
# encoding: utf-8

"""
symmetric-tree.py
 
Created by Shuailong on 2016-02-18.

https://leetcode.com/problems/symmetric-tree/.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

class Solution(object):
    def isSubTreeSymmetric(self, subtree1, subtree2):
        if subtree1 is None and subtree2 is None:
            return True
        if subtree1 is None or subtree2 is None:
            return False
        if subtree1.val != subtree2.val:
            return False
        res = self.isSubTreeSymmetric(subtree1.left, subtree2.right) \
            and self.isSubTreeSymmetric(subtree1.right, subtree2.left)

        return res

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        res = self.isSubTreeSymmetric(root.left, root.right)

        return res



def main():
    n1 = TreeNode(1)
    # n2 = TreeNode(2)
    # n3 = TreeNode(2)
    # n4 = TreeNode(3)
    # n5 = TreeNode(4)
    # n6 = TreeNode(4)
    # n7 = TreeNode(3)

    root = n1
    # n1.left = n2
    # n1.right = n3
    # n2.left = n4
    # n2.right = n5
    # n3.left = n6
    # n3.right = n7

    solution = Solution()
    print solution.isSymmetric(root)

    n6 = TreeNode(1)
    n7 = TreeNode(2)
    n8 = TreeNode(2)
    n9 = TreeNode(3)
    n10 = TreeNode(3)

    n6.left = n7
    n6.right = n8
    n7.right = n9
    n8.right = n10
    root = n6
    print solution.isSymmetric(root)

    
if __name__ == '__main__':
    main()

        