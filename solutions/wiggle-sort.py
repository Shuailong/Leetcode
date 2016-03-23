#!/usr/bin/env python
# encoding: utf-8

"""
wiggle-sort.py
 
Created by Shuailong on 2016-03-23.

https://leetcode.com/problems/wiggle-sort/.

"""

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums)-1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        

def main():
    solution = Solution()
    nums = [3,5,2,1,6,4]
    solution.wiggleSort(nums)
    print nums
    
if __name__ == '__main__':
    main()

        