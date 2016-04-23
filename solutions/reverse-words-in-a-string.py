#!/usr/bin/env python
# encoding: utf-8

"""
reverse-words-in-a-string.py

Created by Shuailong on 2016-04-23.

https://leetcode.com/problems/reverse-words-in-a-string/.

"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(list(reversed(s.split())))


def main():
    solution = Solution()
    s = 'the sky is blue'
    print solution.reverseWords(s)


if __name__ == '__main__':
    main()
