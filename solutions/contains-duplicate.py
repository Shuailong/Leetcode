#!/usr/bin/env python
# encoding: utf-8

"""
contains-duplicate.py
 
Created by Shuailong on 2016-02-04.

https://leetcode.com/problems/contains-duplicate/.

"""

from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c = Counter(nums)
        if len(c) != len(nums):
        	return True
        return False

def main():
    solution = Solution()
    nums = []
    print solution.containsDuplicate(nums)
    
if __name__ == '__main__':
    main()

        