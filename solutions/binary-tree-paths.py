#!/usr/bin/env python
# encoding: utf-8

"""
binary-tree-paths.py
 
Created by Shuailong on 2016-03-04.

https://leetcode.com/problems/binary-tree-paths/.

"""

from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePathsList(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]

        lpaths = self.binaryTreePathsList(root.left)
        rpaths = self.binaryTreePathsList(root.right)

        for path in lpaths:
            path.insert(0, root.val)
        for path in rpaths:
            path.insert(0, root.val)

        return lpaths + rpaths   


    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        paths = self.binaryTreePathsList(root)
        for path in paths:
            s = ''
            for i in xrange(len(path)-1):
                s += str(path[i]) + '->'
            s += str(path[len(path)-1])
            res.append(s)

        return res


def main():
    solution = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n2.right = n4

    root = n1
    print solution.binaryTreePaths(root)
    
if __name__ == '__main__':
    main()

        