#!/usr/bin/env python
# encoding: utf-8

"""
paint-house.py
 
Created by Shuailong on 2016-03-29.

https://leetcode.com/problems/paint-house/.

"""

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0
        dp = [[0 for j in range(3)] for i in range(n)]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]

        for k in range(1, n):
            for j in range(3):
                dp[k][j] = min((dp[k-1][i] for i in range(3) if i != j)) + costs[k][j]

        return min(dp[n-1])

def main():
    solution = Solution()
    costs = [[1,2,3],[3,2,4],[1,4,2],[2,4,1]]
    print solution.minCost(costs)
    
if __name__ == '__main__':
    main()

