#!/usr/bin/env python
# encoding: utf-8

"""
valid-sudoku.py
 
Created by Shuailong on 2016-01-16.

https://leetcode.com/problems/valid-sudoku/.

"""

from collections import Counter
class Solution(object):
    def allUnique(self, nums):
        '''
        :type nums: List[str]
        :rtype: bool
        '''
        count = Counter(nums)
        for num in count:
            if num != '.' and count[num] > 1:
                return False
        return True
        
    def getNumsFromStart(self, nums, start):
        '''
        :type nums: List[List[str]]
        :type start: (int, int)
        :rtype List[str]
        '''
        x, y = start
        return nums[x][y:y+3] + nums[x+1][y:y+3] + nums[x+2][y:y+3]

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if not self.allUnique(row):
                return False
        board_transpose = map(list, zip(*board))
        for row in board_transpose:
            if not self.allUnique(row):
                return False
        starts = []
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                starts.append((i, j))
        for start in starts:
            sub = self.getNumsFromStart(board, start)
            if not self.allUnique(sub):
                return False
        return True

        
def main():
    solution = Solution()
    board = [['5','3','.','.','7','.','.','.','.'],
             ['6','.','.','1','9','5','.','.','.'],
             ['.','9','8','.','.','.','.','6','.'],
             ['8','.','.','.','6','.','.','.','3'],
             ['4','.','.','8','.','3','.','.','1'],
             ['7','.','.','.','2','.','.','.','6'],
             ['.','6','.','.','.','.','2','8','.'],
             ['.','.','.','4','1','9','.','.','5'],
             ['.','.','.','.','8','.','.','7','9']]
    print solution.isValidSudoku(board)
    
if __name__ == '__main__':
    main()

        