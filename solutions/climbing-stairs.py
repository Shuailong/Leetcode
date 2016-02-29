#!/usr/bin/env python
# encoding: utf-8

"""
climbing-stairs.py
 
Created by Shuailong on 2015-11-28.

https://leetcode.com/problems/climbing-stairs/.

"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]



def main():
    n = 4
    solution = Solution()
    print solution.climbStairs(n)
    
if __name__ == '__main__':
    main()

