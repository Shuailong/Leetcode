#!/usr/bin/env python
# encoding: utf-8

"""
sum-of-left-leaves.py

Created by Shuailong on 2016-10-18.

https://leetcode.com/problems/sum-of-left-leaves/.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None:
            return self.sumOfLeftLeaves(root.right)

        if root.left.left is None and root.left.right is None:
            return root.left.val + self.sumOfLeftLeaves(root.right)

        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


def main():
    t1 = TreeNode(3)
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t4 = TreeNode(15)
    t5 = TreeNode(7)

    root = t1
    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5

    solution = Solution()
    print solution.sumOfLeftLeaves(root)



if __name__ == '__main__':
    main()
