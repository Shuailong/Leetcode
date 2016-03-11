#!/usr/bin/env python
# encoding: utf-8

"""
excel-sheet-column-title.py
 
Created by Shuailong on 2016-03-11.

https://leetcode.com/problems/excel-sheet-column-title/.

"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            d = n % 26
            if d == 0:
                d = 26
            alpha = chr(ord('A')+ d - 1)
            res = alpha + res
            n = (n-d) / 26
        return res

def main():
    solution = Solution()
    for i in range(1, 120):
        print i, solution.convertToTitle(i)
    print solution.convertToTitle(1014)
    
if __name__ == '__main__':
    main()

        