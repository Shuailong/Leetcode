#!/usr/bin/env python
# encoding: utf-8

"""
missing-number.py
 
Created by Shuailong on 2016-04-06.

https://leetcode.com/problems/missing-number/.

"""

from operator import xor
class Solution1(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(xor, nums) ^ reduce(xor, range(len(nums)+1))


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return ((1+len(nums))*len(nums) >> 1) - sum(nums)

def main():
    solution = Solution1()
    nums = [0, 1, 2, 3]
    print solution.missingNumber(nums)
    
if __name__ == '__main__':
    main()

        