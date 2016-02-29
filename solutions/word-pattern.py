#!/usr/bin/env python
# encoding: utf-8

"""
word-pattern.py
 
Created by Shuailong on 2016-01-05.

https://leetcode.com/problems/word-pattern/.

"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        words = str.split(' ')
        if len(words) != len(pattern):
            return False

        d = {}
        for i in range(len(pattern)):
            if d.get(pattern[i],'') == '':
                d[pattern[i]] = words[i]
            elif d[pattern[i]] != words[i]:
                return False
        
        flipped = {}
        for j in range(len(words)):
            if flipped.get(words[j],'') == '':
                flipped[words[j]] = pattern[j]
            elif flipped[words[j]] != pattern[j]:
                return False

        return True


def main():
    solution = Solution()
    pattern = "abba"
    str = "dog dog dog dog"
    print solution.wordPattern(pattern, str)
    
if __name__ == '__main__':
    main()

