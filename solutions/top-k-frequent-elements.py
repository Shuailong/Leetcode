#!/usr/bin/env python
# encoding: utf-8

"""
top-k-frequent-elements.py

Created by Shuailong on 2016-05-12.

https://leetcode.com/problems/top-k-frequent-elements/.

"""

from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = Counter(nums)
        return heapq.nlargest(k, c, key=lambda x:c[x])

def main():
    solution = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print solution.topKFrequent(nums, k)


if __name__ == '__main__':
    main()
