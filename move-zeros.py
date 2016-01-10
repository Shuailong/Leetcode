#!/usr/bin/env python
# encoding: utf-8

"""
move-zeros.py
 
Created by Shuailong on 2015-12-21.

https://leetcode.com/problems/prolem/move-zeros/.

"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
                
        while swaped:
            

        

def main():
    solution = Solution()
    nums = [0,1,0,3,12]
    print nums
    solution.moveZeroes(nums)
    print nums
    
if __name__ == '__main__':
    main()

