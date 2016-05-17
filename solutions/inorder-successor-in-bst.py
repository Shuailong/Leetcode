#!/usr/bin/env python
# encoding: utf-8

"""
inorder-successor-in-bst.py

Created by Shuailong on 2016-05-17.

https://leetcode.com/problems/inorder-successor-in-bst/.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def visit(self, root):
        if root is None:
            return []
        return self.visit(root.left) + [root] + self.visit(root.right)

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        inorder = self.visit(root)
        for i in range(len(inorder)):
            if inorder[i] == p and i < len(inorder)-1:
                return inorder[i+1]
        return None


def main():
    solution = Solution()
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
    p = t4

    print p.val
    print solution.inorderSuccessor(root, p).val


if __name__ == '__main__':
    main()
