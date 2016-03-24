#!/usr/bin/env python
# encoding: utf-8

"""
single-number-ii.py
 
Created by Shuailong on 2016-03-23.

https://leetcode.com/problems/single-number-ii/.

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        O(n) time and O(1) space, but slower than Solution1 and Solution2.
        :type nums: List[int]
        :rtype: int
        """
        MAX_LEN = 32
        bit_sums = [0]*32
        
        for i in range(MAX_LEN):
            for num in nums:
                bit_sums[i] += num >> i & 1
        bit_sums = [str(bit_sum % 3) for bit_sum in bit_sums] # bit_nums[:]
        bit_sums.reverse()

        if bit_sums[0] == '0':
            res = int(''.join(bit_sums), 2)
        else:
            bits = ''.join(['1' if bit == '0' else '0' for bit in bit_sums])
            res = -(int(bits, 2) + 1)
        return res
    

from collections import Counter
class Solution2(object):
    def singleNumber(self, nums):
        """
        Use extra space. 52ms
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
        Not linear time. 60ms.
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0, len(nums)-2, 3):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[len(nums)-1]

def main():
    solution = Solution()
    nums = [1]
    print solution.singleNumber(nums)
    
if __name__ == '__main__':
    main()

        