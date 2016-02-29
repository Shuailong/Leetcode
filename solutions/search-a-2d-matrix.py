#!/usr/bin/env python
# encoding: utf-8

"""
search-a-2d-matrix.py
 
Created by Shuailong on 2016-02-03.

https://leetcode.com/problems/search-a-2d-matrix/.

"""

'''TODO: binary search'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        heads = []
        for row in matrix:
            heads.append(row[0])
        target_row_index = 0
        for i in range(len(heads)):
            if i == len(heads)-1 and heads[i] <= target\
                or i < len(heads)-1 and heads[i] <= target and heads[i+1] > target:
                target_row_index = i
                break
        target_row = matrix[target_row_index]
        for i in range(len(target_row)):
            if target_row[i] == target:
                return True
        return False


        

def main():
    solution = Solution()
    m = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 3
    m = [[1,2],[3,5]]
    target = 5
    print solution.searchMatrix(m, target)
    
if __name__ == '__main__':
    main()

        