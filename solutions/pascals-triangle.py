#!/usr/bin/env python
# encoding: utf-8

"""
pascals-triangle.py
 
Created by Shuailong on 2016-02-20.

https://leetcode.com/problems/pascals-triangle/.

"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            row = [0]*(i+1)
            for j in range(i+1):
                if j == 0 or j == i:
                    row[j] = 1
                else:
                    row[j] = res[i-1][j] + res[i-1][j-1]
            res.append(row)
        return res

def main():
    solution = Solution()
    numRows = 5
    print solution.generate(5)
    
if __name__ == '__main__':
    main()

        