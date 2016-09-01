#!/usr/bin/env python
# encoding: utf-8

"""
find-the-difference.py

Created by Shuailong on 2016-09-01.

https://leetcode.com/problems/find-the-difference/.

"""

# 56ms

from operator import xor


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        return chr(reduce(xor, [ord(i) for i in s+t]))


def main():
    s = 'abcd'
    t = 'abcde'
    solution = Solution()
    print solution.findTheDifference(s, t)


if __name__ == '__main__':
    main()
