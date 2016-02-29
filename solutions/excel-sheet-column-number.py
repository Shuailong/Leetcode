#!/usr/bin/env python
# encoding: utf-8

"""
excel-sheet-column-number.py
 
Created by Shuailong on 2016-02-04.

https://leetcode.com/problems/excel-sheet-column-number/.

"""

class Solution(object):
    def getValue(self, ch):
        return ord(ch) - ord('A') + 1
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        v = 0
        for c in s:
            d = self.getValue(c)
            v = v * 26 + d
        return v


        
def main():
    solution = Solution()
    s = 'AB'
    print solution.titleToNumber(s)
    
if __name__ == '__main__':
    main()

        