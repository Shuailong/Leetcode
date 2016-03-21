#!/usr/bin/env python
# encoding: utf-8

"""
zigzag-conversion.py
 
Created by Shuailong on 2016-01-15.

https://leetcode.com/problems/zigzag-conversion/.

"""

'''
Key: understand the problem.
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = [''] * numRows
        period = numRows + (numRows - 2)
        for i in range(len(s)):
            floor = i % period
            if floor > period/2:
                floor = period - floor
            res[floor] += s[i]
        return ''.join(res)



def main():
    solution = Solution()
    s = 'PAYPALISHIRING'
    numRows = 3 
    print solution.convert(s, numRows) == 'PAHNAPLSIIGYIR'
    
if __name__ == '__main__':
    main()

