#!/usr/bin/env python
# encoding: utf-8

"""
find-leaves-of-binary-tree.py

Created by Shuailong on 2016-09-01.

https://leetcode.com/problems/find-leaves-of-binary-tree/.

"""

# 70.46%


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isNone(self, root):
        return root is None or root.val is None

    def isLeaf(self, root):
        return not self.isNone(root) and self.isNone(root.left) and self.isNone(root.right)

    def leaves(self, root):
        if self.isNone(root):
            return []
        if self.isLeaf(root):
            val = root.val
            root.val = None
            return [val]
        return self.leaves(root.left) + self.leaves(root.right)

    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        while True:
            leaves = self.leaves(root)
            if len(leaves) == 0:
                break
            ret.append(leaves)

        return ret


def main():
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    root = t1

    solution = Solution()
    print solution.findLeaves(root)

if __name__ == '__main__':
    main()
