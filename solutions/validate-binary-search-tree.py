#!/usr/bin/env python
# encoding: utf-8

"""
validate-binary-search-tree.py

Created by Shuailong on 2016-05-28.

https://leetcode.com/problems/validate-binary-search-tree/.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def largest(self, root):
        p = root
        while p.right is not None:
            p = p.right
        return p.val

    def smallest(self, root):
        p = root
        while p.left is not None:
            p = p.left
        return p.val

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is not None and root.right is not None:
            return self.isValidBST(root.left) and self.isValidBST(root.right) \
                and self.largest(root.left) < root.val\
                and self.smallest(root.right) > root.val
        if root.left is not None:
            return self.isValidBST(root.left) and self.largest(root.left) < root.val
        else:
            return self.isValidBST(root.right) and self.smallest(root.right) > root.val


def main():
    t1 = TreeNode(2)
    t2 = TreeNode(1)
    t3 = TreeNode(3)
    root = t1
    t1.left = t2
    t1.right = t3
    solution = Solution()
    print solution.isValidBST(root)


if __name__ == '__main__':
    main()
