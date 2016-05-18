#!/usr/bin/env python
# encoding: utf-8

"""
search-insert-position.py

Created by Shuailong on 2016-05-18.

https://leetcode.com/problems/search-insert-position/.

"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)/2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return l


def main():
    solution = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    print solution.searchInsert(nums, target)
    target = 2
    print solution.searchInsert(nums, target)
    target = 7
    print solution.searchInsert(nums, target)
    target = 0
    print solution.searchInsert(nums, target)


if __name__ == '__main__':
    main()
