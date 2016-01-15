#!/usr/bin/env python
# encoding: utf-8

"""
maximum-size-subarray-sum-equals-k.py
 
Created by Shuailong on 2016-01-06.

https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/.

"""

'''Not solved yet.'''

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        


class Solution2(object):
    '''TLE'''
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        max_length = 0
        for start_index in range(n):
            this_length = 0
            subsum = 0
            j = start_index
            while j < n:
                subsum += nums[j]
                if subsum == k:
                    this_length = j - start_index + 1
                j += 1
            if this_length > max_length:
                max_length = this_length

        return max_length


class Solution1(object):
    '''TLE'''
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        for length in range(n,0,-1):   
            for start_index in range(n-length+1):
                subsum = 0
                for i in range(length):
                    subsum += nums[start_index+i]
                if subsum == k:
                    return length
        return 0


def main():
    solution = Solution()
    nums = [1, -1, 5, -2, 3]
    k = 3
    print solution.maxSubArrayLen(nums,k)
    nums = [-2, -1, 2, 1]
    k = 1
    print solution.maxSubArrayLen(nums,k)

    
if __name__ == '__main__':
    main()

        