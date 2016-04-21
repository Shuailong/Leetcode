#!/usr/bin/env python
# encoding: utf-8

"""
house-robber-ii.py
 
Created by Shuailong on 2016-04-13.

https://leetcode.com/problems/house-robber-ii/.

"""

class Solution(object):
    def rob1(self, nums):
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

        s = [False]*n

        s[0] = True
        if dp[1] == nums[1]:
            s[1] = True

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            if dp[i] != dp[i-1]:
                s[i] = True
        
        rob_num = []
        i = n-1
        while i >= 0:
            if s[i]:
                rob_num.append(i)
                i -= 2
            else:
                i -= 1

        if 0 in rob_num and n-1 in rob_num:
            return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))
        else:
            return dp[n-1]
        

def main():
    nums = [2,1,1,2]
    solution = Solution()
    print solution.rob(nums)
    
if __name__ == '__main__':
    main()

