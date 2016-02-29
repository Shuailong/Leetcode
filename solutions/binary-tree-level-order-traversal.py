#!/usr/bin/env python
# encoding: utf-8

"""
binary-tree-level-order-traversal.py
 
Created by Shuailong on 2016-02-19.

https://leetcode.com/problems/binary-tree-level-order-traversal/.

"""

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res = []

        queue = deque()
        p = root
        queue.append(p)

        while queue:
            s = len(queue)
            level_nodes = []
            while s:
                p = queue.popleft()
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
                s -= 1
                level_nodes.append(p.val)
            res.append(level_nodes)
        return res


def main():
    n1 = TreeNode(3)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n4 = TreeNode(15)
    n5 = TreeNode(7)

    root = n1
    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5

    solution = Solution()
    print solution.levelOrder(root)
    
if __name__ == '__main__':
    main()

