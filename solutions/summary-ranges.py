#!/usr/bin/env python
# encoding: utf-8

"""
summary-ranges.py
 
Created by Shuailong on 2016-03-08.

https://leetcode.com/problems/summary-ranges/.

"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        tuples = []
        start_idx = 0
        end_idx = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                end_idx += 1
            else:
                tuples.append((nums[start_idx], nums[end_idx]))
                start_idx = i
                end_idx = i

        tuples.append((nums[start_idx], nums[end_idx]))
        res = []
        for t in tuples:
            if t[0] != t[1]:
                res.append(str(t[0]) + '->' + str(t[1]))
            else:
                res.append(str(t[0]))

        return res
        
def main():
    solution = Solution()
    l = [0,1,2,4,5,7]
    print solution.summaryRanges(l)
    
if __name__ == '__main__':
    main()

