#!/usr/bin/env python
# encoding: utf-8

"""
remove-duplicates-from-sorted-array.py
 
Created by Shuailong on 2016-01-15.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/.

"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 2

        p1 = 0
        p2 = 1
        while p2 < len(nums):
            while p2 < len(nums) and nums[p2] == nums[p1]:
                p2 += 1
            if p2 == len(nums):
                break
            p1 += 1
            nums[p1] = nums[p2]
            p2 += 1
        
        return p1+1

        
        

def main():
    solution = Solution()
    nums = [1]

    print solution.removeDuplicates(nums)
    print nums
    
if __name__ == '__main__':
    main()

