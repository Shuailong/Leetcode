#!/usr/bin/env python
# encoding: utf-8

"""
valid-sudoku.py
 
Created by Shuailong on 2016-01-16.

https://leetcode.com/problems/valid-sudoku/.

"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
        	count = {}
        	for d in row:
        		if d != '.':
        			num = int(d)
        			count[num] = count.get(num,0) + 1
        	for k in count:
        		if count[k] != 1 and count[k] != 0:
        			return False
        



def main():
    solution = Solution()
    print isValidSudoku()
    
if __name__ == '__main__':
    main()

        