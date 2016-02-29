#!/usr/bin/env python
# encoding: utf-8

"""
unique-paths-ii.py
 
Created by Shuailong on 2015-11-28.

https://leetcode.com/problems/unique-paths-ii/.

"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[m-1][n-1] == 1:
            return 0

        dp = [[0 for i in range(n+1)] for i in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    if obstacleGrid[i-1][j-1] == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                elif obstacleGrid[i-1][j-2] == 0 and obstacleGrid[i-2][j-1] == 0:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
                elif obstacleGrid[i-1][j-2] == 0:
                    dp[i][j] = dp[i][j-1]
                elif obstacleGrid[i-2][j-1] == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = 0
        return dp[m][n]


def main():
    # obstacleGrid = [
    #       [0,0,0],
    #       [0,1,0],
    #       [0,0,0]
    #     ]
    obstacleGrid = [[1, 0]]
    solution = Solution()
    print solution.uniquePathsWithObstacles(obstacleGrid) 
    
if __name__ == '__main__':
    main()

        