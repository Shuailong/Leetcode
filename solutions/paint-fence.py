#!/usr/bin/env python
# encoding: utf-8

"""
paint-fence.py
 
Created by Shuailong on 2016-01-18.

https://leetcode.com/problems/paint-fence/.

"""

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [0]*(n+1)
        if n == 0:
            return 0
        dp[1] = k
        if n == 1:
            return dp[1]
        dp[2] = k**2
        if n == 2:
            return dp[2]
        dp[3] = k*(k-1)+k*k*(k-1)
        if n == 3:
            return dp[3]
        for i in range(4, n+1):
            dp[i] = dp[i-3]*(k-1)*(k-1)+dp[i-2]*(k-1)*k

        return dp[n]


def main():
    solution = Solution()
    n = 0
    k = 2
    print solution.numWays(n,k)
    
if __name__ == '__main__':
    main()

