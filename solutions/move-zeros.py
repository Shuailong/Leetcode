#!/usr/bin/env python
# encoding: utf-8

"""
move-zeros.py
 
Created by Shuailong on 2015-12-21.

https://leetcode.com/problems/move-zeros/.

"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0
        count_zeros = 0
        while p2 < len(nums):
            if nums[p2] != 0:
                nums[p1] = nums[p2]
                p1 += 1
            else:
                count_zeros += 1
            p2 += 1
        while p1 < len(nums):
            nums[p1] = 0
            p1 += 1
            

        

def main():
    solution = Solution()
    nums = [0,1,0,3,12]
    print nums
    solution.moveZeroes(nums)
    print nums
    
if __name__ == '__main__':
    main()

