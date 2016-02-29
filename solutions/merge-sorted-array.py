#!/usr/bin/env python
# encoding: utf-8

"""
merge-sorted-array.py
 
Created by Shuailong on 2016-02-27.

https://leetcode.com/problems/merge-sorted-array/.

"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        p = m+n-1
        while p1 >=0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        while p1 >= 0:
            nums1[p] = nums1[p1]
            p1 -= 1
            p -= 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
        # print nums1

def main():
    nums1 = [3,6,7]
    m = len(nums1)
    nums2 = [2,4,8,10,12]
    n = len(nums2)
    nums1 += [None]*n
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    
if __name__ == '__main__':
    main()

        