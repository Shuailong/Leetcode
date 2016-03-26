#!/usr/bin/env python
# encoding: utf-8

"""
swap-nodes-in-pairs.py
 
Created by Shuailong on 2016-03-25.

https://leetcode.com/problems/swap-nodes-in-pairs/.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        p = dummy

        while p.next and p.next.next:
            tmp = p.next.next.next
            p1 = p.next
            p2 = p1.next
            p.next = p2
            p2.next = p1
            p1.next = tmp
            p = p1

        return dummy.next
        

def main():
    solution = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    new_head = solution.swapPairs(head)
    while new_head:
    	print new_head.val,
    	new_head = new_head.next
    	
if __name__ == '__main__':
    main()

        