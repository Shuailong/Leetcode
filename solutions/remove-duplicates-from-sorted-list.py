#!/usr/bin/env python
# encoding: utf-8

"""
remove-duplicates-from-sorted-list.py
 
Created by Shuailong on 2016-02-15.

https://leetcode.com/problems/remove-duplicates-from-sorted-list/.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        p1 = head
        p2 = head.next
        while p1 is not None and p2 is not None:
            while p2 is not None and p1.val == p2.val:
                p2 = p2.next
            p1.next = p2
            p1 = p2
            if p2 is None:
                break
            p2 = p2.next
        return head
        

def main():
    solution = Solution()
    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(1)
    n4 = ListNode(1)
    n5 = ListNode(1)

    head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    new_head = solution.deleteDuplicates(head)
    p = new_head
    while p is not None:
        print p,
        p = p.next

    
if __name__ == '__main__':
    main()

        