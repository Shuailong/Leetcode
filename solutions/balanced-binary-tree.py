#!/usr/bin/env python
# encoding: utf-8

"""
balanced-binary-tree.py
 
Created by Shuailong on 2016-02-17.

https://leetcode.com/problems/balanced-binary-tree/.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def depth(self, node):
        if node is None:
            return 0
        return max(self.depth(node.left), self.depth(node.right))+1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None or abs(self.depth(root.left) - self.depth(root.right)) <= 1 \
            and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False


def main():
    n1 = TreeNode(1)
    n2 = TreeNode(1)
    n3 = TreeNode(1)
    n4 = TreeNode(1)
    n5 = TreeNode(1)
    n6 = TreeNode(1)
    n7 = TreeNode(1)

    root = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n3.right = n5
    n4.left = n6
    n5.right = n7


    solution = Solution()
    print solution.isBalanced(n1)
    
if __name__ == '__main__':
    main()

        