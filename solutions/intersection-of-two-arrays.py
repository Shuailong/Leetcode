#!/usr/bin/env python
# encoding: utf-8

"""
intersection-of-two-arrays.py

Created by Shuailong on 2016-05-27.

https://leetcode.com/problems/intersection-of-two-arrays/.

"""

from collections import Counter


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        res = []
        for key in c1:
            if key in c2:
                res.append(key)
        return res


def main():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    solution = Solution()
    print solution.intersection(nums1, nums2)


if __name__ == '__main__':
    main()
