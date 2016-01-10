#!/usr/bin/env python
# encoding: utf-8

"""
house-robber.py
 
Created by Shuailong on 2015-11-28.

https://leetcode.com/problems/house-robber/.

"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    
        return dp[n-1]
        


def main():
    nums = [20, 2, 1, 10, 9, 2]
    solution = Solution()
    print solution.rob(nums)
    
if __name__ == '__main__':
    main()

