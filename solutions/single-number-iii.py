#!/usr/bin/env python
# encoding: utf-8

"""
single-number-iii.py
 
Created by Shuailong on 2016-03-29.

https://leetcode.com/problems/single-number-iii/.

"""

'''Key: divide numbers into two groups to separate two distinct numbers.'''

from operator import xor
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = reduce(xor, nums)
        x = s & -s
        n1 = reduce(xor, (num for num in nums if num & x))
        return n1, s^n1
        
def main():
    solution = Solution()
    nums = [1,2,1,3,2,5]
    print solution.singleNumber(nums)
    
if __name__ == '__main__':
    main()

