#!/usr/bin/env python
# encoding: utf-8

"""
majority-element.py
 
Created by Shuailong on 2016-02-10.

https://leetcode.com/problems/majority-element/.

"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]


        

def main():
    solotion = Solution()
    nums = [1,1,2,3,3,3,2,3,3,3,2,2,2,2,2,2,2,2]
    print solotion.majorityElement(nums)
    
if __name__ == '__main__':
    main()

        