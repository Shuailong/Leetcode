#!/usr/bin/env python
# encoding: utf-8

"""
unique-paths.py
 
Created by Shuailong on 2015-11-28.

https://leetcode.com/problems/unique-paths/.

"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n+1)] for i in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 or j == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m][n]

def main():
    m = 100
    n = 100
    solution = Solution()
    print solution.uniquePaths(m, n) 
    
if __name__ == '__main__':
    main()

        