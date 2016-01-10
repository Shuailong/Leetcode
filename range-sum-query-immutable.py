#!/usr/bin/env python
# encoding: utf-8

"""
range-sum-query-immutable.py
 
Created by Shuailong on 2015-11-27.

https://leetcode.com/problems/range-sum-query-immutable/.

"""


class NumArray(object):

    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        n = len(nums)
        if n == 0:
            return
        self.sums = [0]*n
        self.sums[0] = nums[0]
        for i in range(1, n):
            self.sums[i] = self.sums[i-1] + nums[i]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i-1<0:
            return self.sums[j]
        return self.sums[j] - self.sums[i-1];


def main():
    # Your NumArray object will be instantiated and called as such:
    nums = [-2, 0, 3, -5, 2, -1]
    numArray = NumArray(nums)
    print numArray.sumRange(0, 2)
    print numArray.sumRange(2, 5)
    print numArray.sumRange(0, 5)
    
if __name__ == '__main__':
    main()

