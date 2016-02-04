#!/usr/bin/env python
# encoding: utf-8

"""
valid-anagram.py
 
Created by Shuailong on 2016-02-04.

https://leetcode.com/problems/valid-anagram/.

"""

from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        c1 = Counter(s)
        c2 = Counter(t)
        return c1 == c2
        

def main():
    solution = Solution()
    s = 'anagram'
    t = 'nagaram'
    print solution.isAnagram(s,t)
    
if __name__ == '__main__':
    main()

        