#!/usr/bin/env python
# encoding: utf-8

"""
remove-nth-node-from-end-of-list.py
 
Created by Shuailong on 2016-01-15.

https://leetcode.com/problems/remove-nth-node-from-end-of-list/.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = head
        p2 = head
        for i in range(n):
            p2 = p2.next

        if p2 == None:
            return p1.next
        
        while p2.next != None:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next
        return head
    

def main():
    solution = Solution()
    solution.removeNthFromEnd(head, n)
    
if __name__ == '__main__':
    main()

