#!/usr/bin/env python
# encoding: utf-8

"""
two-sum.py
 
Created by Shuailong on 2016-03-10.

https://leetcode.com/problems/two-sum/.

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {num: 0 for num in nums}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in d:
                continue
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


def main():
    solution = Solution()
    nums = [2,7,11,15]
    target = 13
    print solution.twoSum(nums, target)
    
if __name__ == '__main__':
    main()

