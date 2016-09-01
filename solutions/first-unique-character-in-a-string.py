#!/usr/bin/env python
# encoding: utf-8

"""
first-unique-character-in-a-string.py

Created by Shuailong on 2016-09-01.

https://leetcode.com/problems/first-unique-character-in-a-string/.

"""

# 376 ms

from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = Counter(s)
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        return -1


def main():
    solution = Solution()
    print solution.firstUniqChar('leetcode')
    print solution.firstUniqChar('loveleetcode')


if __name__ == '__main__':
    main()
