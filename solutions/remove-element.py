#!/usr/bin/env python
# encoding: utf-8

"""
remove-element.py
 
Created by Shuailong on 2016-01-16.

https://leetcode.com/problems/remove-element/.

"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p1 = 0
        p2 = 0
        while p2 < len(nums):
            while p2 < len(nums) and nums[p2] == val:
                p2 += 1
            if p2 == len(nums):
                break
            nums[p1] = nums[p2]
            p1 += 1
            p2 += 1

        return p1

        

def main():
    solution = Solution()
    nums = [1]
    val = 4
    print solution.removeElement(nums, val)
    print nums
    
if __name__ == '__main__':
    main()

        