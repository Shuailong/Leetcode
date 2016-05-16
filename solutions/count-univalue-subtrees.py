#!/usr/bin/env python
# encoding: utf-8

"""
count-univalue-subtrees.py

Created by Shuailong on 2016-05-15.

https://leetcode.com/problems/count-univalue-subtrees/.

"""

'''TODO: performance need improving.'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isUnivalSubtree(self, root):
        '''
        :type root: TreeNode
        :rtype: int | None
        '''

        if root is None:
            return None
        if root.left is None and root.right is None:
            return root.val

        lval = self.isUnivalSubtree(root.left)
        rval = self.isUnivalSubtree(root.right)

        if root.val == lval and root.val == rval:
            return root.val

        if root.left is None and root.val == rval or root.right is None and root.val == lval:
            return root.val

        return None

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        res = self.countUnivalSubtrees(root.left) + self.countUnivalSubtrees(root.right)
        if self.isUnivalSubtree(root):
            res += 1
        return res


def main():
    solution = Solution()
    t1 = TreeNode(5)
    t2 = TreeNode(1)
    t3 = TreeNode(5)
    t4 = TreeNode(5)
    t5 = TreeNode(5)
    t6 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.right = t6
    root = t1
    print solution.countUnivalSubtrees(root)


if __name__ == '__main__':
    main()
