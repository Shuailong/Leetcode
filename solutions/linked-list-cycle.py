#!/usr/bin/env python
# encoding: utf-8

"""
linked-list-cycle.py

Created by Shuailong on 2016-04-23.

https://leetcode.com/problems/linked-list-cycle/.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        p1 = p2 = head
        p1 = p1.next
        if p1 is None:
            return False

        p2 = p2.next.next
        while p1 != p2:
            if p1 is None:
                return False
            p1 = p1.next
            if p2 is None or p2.next is None:
                return False
            p2 = p2.next.next

        return True


def main():
    pass


if __name__ == '__main__':
    main()
