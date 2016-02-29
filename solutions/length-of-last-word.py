#!/usr/bin/env python
# encoding: utf-8

"""
length-of-last-word.py
 
Created by Shuailong on 2016-01-16.

https://leetcode.com/problems/length-of-last-word/.

"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        s = s.rstrip()
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                count += 1
            else:
                break
        return count

def main():
    solution = Solution()
    s = "Hello"
    print solution.lengthOfLastWord(s)
    
if __name__ == '__main__':
    main()

        