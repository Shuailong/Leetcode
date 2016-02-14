#!/usr/bin/env python
# encoding: utf-8

"""
reverse-linked-list.py
 
Created by Shuailong on 2016-02-13.

https://leetcode.com/problems/reverse-linked-list/.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)

class Solution(object):
    """Iterative solution"""
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        p1 = head
        p2 = head.next

        p1.next = None
        while p2 != None:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp

        return p1
        
class Solution2(object):
    """Recursive solution"""
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        p1 = head
        p2 = head.next
        p1.next = None
        if p2 is None:
            return p1
        tmp = p2
        new_head = self.reverseList(p2)
        tmp.next = p1
        return new_head
        


def main():
    solution = Solution2()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    head = n1
    n1.next = n2
    n2.next = n3

    new_head = solution.reverseList(head)
    print new_head, new_head.next, new_head.next.next, new_head.next.next.next

    
if __name__ == '__main__':
    main()

