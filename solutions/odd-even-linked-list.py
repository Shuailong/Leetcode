#!/usr/bin/env python
# encoding: utf-8

"""
odd-even-linked-list.py
 
Created by Shuailong on 2016-02-15.

https://leetcode.com/problems/odd-even-linked-list/.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = head
        if p1 is None:
            return None
        p2 = head.next
        if p2 is None:
            return head
        even_head = head.next
        while p1.next is not None and p1.next.next is not None:
            p1.next = p1.next.next
            p2.next = p2.next.next
            p1 = p1.next
            p2 = p2.next

        p1.next = even_head
        return head

def main():
    solution = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    new_head = solution.oddEvenList(head)
    p = new_head
    while p is not None:
        print p,
        p = p.next

    
if __name__ == '__main__':
    main()

        