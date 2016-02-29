#!/usr/bin/env python
# encoding: utf-8

"""
unique-binary-search-trees.py
 
Created by Shuailong on 2015-11-28.

https://leetcode.com/problems/unique-binary-search-trees/

"""

from math import factorial

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, n+1):
            dp[i] = 0
            for j in range(0, i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]

class Solution2(object):
    """ Catalan number """
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        return factorial(2*n)/factorial(n+1)/factorial(n)
        

def main():
    n = 3
    solution = Solution2()
    print solution.numTrees(n)
    
if __name__ == '__main__':
    main()

        