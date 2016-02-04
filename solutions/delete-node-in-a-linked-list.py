#!/usr/bin/env python
# encoding: utf-8

"""
delete-node-in-a-linked-list.py
 
Created by Shuailong on 2016-02-04.

https://leetcode.com/problems/delete-node-in-a-linked-list/.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        

def main():
    pass
    
if __name__ == '__main__':
    main()

        