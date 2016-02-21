#!/usr/bin/env python
# encoding: utf-8

"""
path-sum.py
 
Created by Shuailong on 2016-02-21.

https://leetcode.com/problems/path-sum/.

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

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if root is None:
            return False
        if not root.left and not root.right:
            if root.val == sum:
                return True
            else:
                return False

        residual = sum - root.val
        return self.hasPathSum(root.left,residual) or self.hasPathSum(root.right, residual)

        
        
def main():
    n1 = TreeNode(5)
    n2 = TreeNode(4)
    n3 = TreeNode(8)
    n4 = TreeNode(11)
    n5 = TreeNode(13)
    n6 = TreeNode(4)
    n7 = TreeNode(7)
    n8 = TreeNode(2)
    n9 = TreeNode(1)

    root = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n3.left = n5
    n3.right = n6
    n4.left = n7
    n4.right = n8
    n6.right = n9

    solution = Solution()
    sums = [27, 22, 26, 18, 0, 8, 9, 13, 17, 20]
    # 9 and 17
    for sum in sums:
        print solution.hasPathSum(root, sum)
    
    
if __name__ == '__main__':
    main()

