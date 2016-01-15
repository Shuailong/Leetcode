#!/usr/bin/env python
# encoding: utf-8

"""
merge-two-sorted-lists.py
 
Created by Shuailong on 2016-01-15.

https://leetcode.com/problems/merge-two-sorted-lists/.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None

        if l1 == None:
            return l2
        if l2 == None:
            return l1

        i = l1
        j = l2

        if l1.val < l2.val:
            head = l1
            i = l1.next
        else:
            head = l2
            j = l2.next

        p = head
        
        while i != None and j != None:
            if i.val < j.val:
                p.next = i
                p = p.next
                i = i.next
            else:
                p.next = j
                p = p.next
                j = j.next

        if i == None:
            while j != None:
                p.next = j
                p = p.next
                j = j.next
        else:
            while i != None:
                p.next = i
                p = p.next
                i = i.next

        return head

def main():
    solution = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(5)
    head = solution.mergeTwoLists(l1,l2)
    while head != None:
        print head.val,
        head = head.next
    
if __name__ == '__main__':
    main()

