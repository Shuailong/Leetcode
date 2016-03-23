#!/usr/bin/env python
# encoding: utf-8

"""
single-number.py
 
Created by Shuailong on 2016-03-23.

https://leetcode.com/problems/single-number/.

"""

from operator import xor
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(xor, nums)

from collections import Counter
class Solution2(object):
    def singleNumber(self, nums):
        """
        Slower than Solution1. Use extra space.

        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        for k in c:
            if c[k] == 1:
                return k

class Solution1(object):
    def singleNumber(self, nums):
        """
        Not linear time.

        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[len(nums)-1]
        

def main():
    solution = Solution()
    nums = [4, 7, 9, 3, 1, 3, 1, 4, 7, 5, 5, 6, 8, 10, 6, 8, 2, 2, 9]
    print nums
    print solution.singleNumber(nums)
    
if __name__ == '__main__':
    main()

        