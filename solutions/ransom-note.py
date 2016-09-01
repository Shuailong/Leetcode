#!/usr/bin/env python
# encoding: utf-8

"""
ransom-note.py

Created by Shuailong on 2016-09-01.

https://leetcode.com/problems/ransom-note/.

"""

# 217ms

from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r = Counter(ransomNote)
        m = Counter(magazine)
        for i in r:
            if i not in m or r[i] > m[i]:
                return False
        return True


def main():
    solution = Solution()
    print solution.canConstruct('a', 'b')
    print solution.canConstruct('aa', 'ab')
    print solution.canConstruct('aa', 'aab')


if __name__ == '__main__':
    main()
