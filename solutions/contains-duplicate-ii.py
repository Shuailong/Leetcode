#!/usr/bin/env python
# encoding: utf-8

"""
contains-duplicate-ii.py
 
Created by Shuailong on 2016-03-01.

https://leetcode.com/problems/contains-duplicate-ii/.

"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        pos = {}
        for i in range(len(nums)):
            num = nums[i]
            if pos.has_key(num) and i - pos[num] <= k:
                return True
            else:
                pos[num] = i

        return False
        

def main():
    solution = Solution()
    nums = [1,2,3,4,5,6,2,8,9,10]
    k = 4
    print solution.containsNearbyDuplicate(nums, k)
    
if __name__ == '__main__':
    main()

        
