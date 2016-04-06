#!/usr/bin/env python
# encoding: utf-8

"""
missing-number.py
 
Created by Shuailong on 2016-04-06.

https://leetcode.com/problems/missing-number/.

"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = sum(nums)
        m = max(nums)
        if 0 not in nums:
            # the first number not present
            return 0
        elif s == n*(n-1)/2:
            # the last number not present
            return m+1
        else:
            # someone in the middle not present
            return (1+m)*n/2-s

def main():
    solution = Solution()
    nums = [0, 1, 3]
    print solution.missingNumber(nums)
    
if __name__ == '__main__':
    main()

        