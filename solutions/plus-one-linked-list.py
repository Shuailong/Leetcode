#!/usr/bin/env python
# encoding: utf-8

"""
plus-one-linked-list.py

Created by Shuailong on 2016-09-02.

https://leetcode.com/problems/plus-one-linked-list/.

"""

# 44ms for both solutions
# TODO: try reverse - add - reverse.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        val = 0
        while p:
            val = val * 10 + p.val
            p = p.next
        val += 1
        d = []
        while val:
            d.append(val % 10)
            val /= 10
        nhead = ListNode(0)
        p = nhead
        for i in reversed(d):
            p.next = ListNode(i)
            p = p.next
        return nhead.next

    def plusRec(self, head):
        if head is None:
            return 1

        carry = self.plusRec(head.next)
        if carry == 1:
            head.val += 1
            if head.val == 10:
                head.val %= 10
                return 1
        return 0

    def plusOneV2(self, head):
        '''
        recursive solution inspired by the discussion
        '''
        carry = self.plusRec(head)
        if carry == 1:
            nhead = ListNode(1)
            nhead.next = head
            return nhead
        else:
            return head


def main():
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    p = solution.plusOneV2(head)
    while p:
        print p.val,
        p = p.next


if __name__ == '__main__':
    main()
