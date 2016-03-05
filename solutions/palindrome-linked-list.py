#!/usr/bin/env python
# encoding: utf-8

"""
palindrome-linked-list.py
 
Created by Shuailong on 2016-03-05.

https://leetcode.com/problems/palindrome-linked-list/.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

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

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        count = 0
        while p:
            p = p.next
            count += 1
        m = count/2
        p = head
        for i in range(m):
            p = p.next
        p_backward = self.reverseList(p)
        p_forward = head
        for i in range(m):
            if p_forward.val != p_backward.val:
                return False
            p_backward = p_backward.next
            p_forward = p_forward.next

        return True


def main():
    solution = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(2)
    n5 = ListNode(1)
    head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    print solution.isPalindrome(head)

    
if __name__ == '__main__':
    main()

