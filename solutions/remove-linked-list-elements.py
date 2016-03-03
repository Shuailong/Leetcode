#!/usr/bin/env python
# encoding: utf-8

"""
remove-linked-list-elements.py
 
Created by Shuailong on 2016-03-03.

https://leetcode.com/problems/remove-linked-list-elements/.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        while head and head.val == val:
            head = head.next
        p = head
        if head is None:
            return None
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
            if p is None:
                break
        return head


def main():
    solution = Solution()
    p1 = ListNode(1)
    p2 = ListNode(1)
    p3 = ListNode(1)
    p4 = ListNode(1)
    p5 = ListNode(1)
    p6 = ListNode(1)
    p7 = ListNode(1)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p5.next = p6
    p6.next = p7
    head = p1
    val = 1

    p = solution.removeElements(head, val)
    while p:
        print p.val,
        p = p.next
if __name__ == '__main__':
    main()

