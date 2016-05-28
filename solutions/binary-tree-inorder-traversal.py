#!/usr/bin/env python
# encoding: utf-8

"""
binary-tree-inorder-traversal.py

Created by Shuailong on 2016-05-28.

https://leetcode.com/problems/binary-tree-inorder-traversal/.

"""

'''Understand the iterative procedure.'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        stack = []
        while root is not None:
            stack.append(root)
            root = root.left
            while root is None:
                if len(stack) == 0:
                    return res
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res


def main():
    solution = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    root = t1
    t1.right = t2
    t2.left = t3

    print solution.inorderTraversal(root)


if __name__ == '__main__':
    main()
