#!/usr/bin/env python
# encoding: utf-8

"""
intersection-of-two-linked-lists.py
 
Created by Shuailong on 2016-02-27.

https://leetcode.com/problems/intersection-of-two-linked-lists/.

"""

'''
Try to find a O(1) space, O(n) time solution.

'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a_nodes = set()
        p_a = headA
        while p_a is not None:
            a_nodes.add(p_a)
            p_a = p_a.next
        p_b = headB
        while  p_b is not None:
            if p_b in a_nodes:
                return p_b
            p_b = p_b.next
        return p_b
        
        
def main():
    a1 = ListNode(0)
    a2 = ListNode(1)
    b1 = ListNode(2)
    b2 = ListNode(3)
    b3 = ListNode(4)
    c1 = ListNode(5)
    c2 = ListNode(6)
    c3 = ListNode(7)

    headA = a1
    headB = b1
    a1.next = a2
    a2.next = c1
    b1.next = b2
    b2.next = b3
    b3.next = c1
    c1.next = c2
    c2.next = c3

    solution = Solution()
    print solution.getIntersectionNode(headA, headB).val

if __name__ == '__main__':
    main()

