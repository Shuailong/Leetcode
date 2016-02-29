#!/usr/bin/env python
# encoding: utf-8

"""
lowest-common-ancestor-of-a-binary-search-tree.py
 
Created by Shuailong on 2016-02-12.

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/.

"""

'''Too time consuming. To be improved.'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return 'val: '+str(self.val)

class Solution(object):
    def isAncestor(self, p, q):
        """
        whether p is an ancestor of q
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        print 2, p, q
        if p is None:
            return False
        if p.left == q or p.right == q:
            return True
        if p == q:
            return True
        return self.isAncestor(p.left, q) or self.isAncestor(p.right, q)

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        print 1
        if root is None:
            return None

        if self.isAncestor(root, p) and self.isAncestor(root, q) and \
            not (self.isAncestor(root.left, p) and self.isAncestor(root.left, q)) and \
            not (self.isAncestor(root.right, p) and self.isAncestor(root.right, q)):
            return root
        res1 = self.lowestCommonAncestor(root.left, p, q)
        if res1 is not None:
            return res1
        res2 = self.lowestCommonAncestor(root.right, p, q) 
        if res2 is not None:
            return res2
        return None
        

def main():
    solution = Solution()

    n1 = TreeNode(6)
    n2 = TreeNode(2)
    n3 = TreeNode(8)
    n4 = TreeNode(0)
    n5 = TreeNode(4)
    n6 = TreeNode(7)
    n7 = TreeNode(9)
    n8 = TreeNode(3)
    n9 = TreeNode(5)

    root = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n5.left = n8
    n5.right = n9

    p = n2
    q = n3
    print solution.lowestCommonAncestor(root, p, q)
    p = n8
    q = n4
    print solution.lowestCommonAncestor(root, p, q)
    
if __name__ == '__main__':
    main()

        