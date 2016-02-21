#!/usr/bin/env python
# encoding: utf-8

"""
pascals-triangle-ii.py
 
Created by Shuailong on 2016-02-20.

https://leetcode.com/problems/pascals-triangle-ii/.

"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        lastrow = []
        row = []

        for i in range(rowIndex+1):
            row = [0]*(i+1)
            for j in range(i+1):
                if j == 0 or j == i:
                    row[j] = 1
                else:
                    row[j] = lastrow[j] + lastrow[j-1]
            lastrow = row
        return row
        

def main():
    solution = Solution()
    print solution.getRow(5)
    
if __name__ == '__main__':
    main()

        