#!/usr/bin/env python
# encoding: utf-8

"""
rotate-array.py
 
Created by Shuailong on 2016-03-12.

https://leetcode.com/problems/rotate-array/.

"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:n] + nums[:n-k]
        

def main():
    solution = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    solution.rotate(nums, k)
    print nums
    
if __name__ == '__main__':
    main()

