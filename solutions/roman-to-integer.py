#!/usr/bin/env python
# encoding: utf-8

"""
roman-to-integer.py
 
Created by Shuailong on 2016-03-17.

https://leetcode.com/problems/roman-to-integer/.

"""

class Solution(object):
    def __init__(self):
        self.d = {'I':1, 'V':5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            res += self.d[s[i]]
            if s[i] == 'I' and i+1 < len(s) and (s[i+1] == 'V' or s[i+1] == 'X'):
                res -= 2
            elif s[i] == 'X' and i+1 < len(s) and (s[i+1] == 'L' or s[i+1] == 'C'):
                res -= 20
            elif s[i] == 'C' and i+1 < len(s) and (s[i+1] == 'D' or s[i+1] == 'M'):
                res -= 200

        return res

        

def main():
    solution = Solution()
    Ss = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    for s in Ss:
        print solution.romanToInt(s)
    
if __name__ == '__main__':
    main()

        