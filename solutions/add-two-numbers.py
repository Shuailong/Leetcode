#!/usr/bin/env python
# encoding: utf-8

"""
add-two-numbers.py

Created by Shuailong on 2016-04-23.

https://leetcode.com/problems/add-two-numbers/.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        s = ListNode(0)
        p = s
        carry = 0
        while p1 and p2:
            p.next = ListNode((p1.val + p2.val + carry) % 10)
            carry = (p1.val + p2.val + carry) / 10
            p1 = p1.next
            p2 = p2.next
            p = p.next
        while p1:
            p.next = ListNode((p1.val + carry) % 10)
            carry = (p1.val + carry) / 10
            p1 = p1.next
            p = p.next
        while p2:
            p.next = ListNode((p2.val + carry) % 10)
            carry = (p2.val + carry) / 10
            p2 = p2.next
            p = p.next
        if carry:
            p.next = ListNode(carry)

        return s.next


def main():
    solution = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    s = solution.addTwoNumbers(l1, l2)
    while s:
        print s.val,
        s = s.next


if __name__ == '__main__':
    main()
