#!/usr/bin/env python
# encoding: utf-8

"""
reverse-string.py

Created by Shuailong on 2016-04-23.

https://leetcode.com/problems/reverse-string/.

"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


def main():
    solution = Solution()
    s = "Hello"
    print solution.reverseString(s)


if __name__ == '__main__':
    main()
