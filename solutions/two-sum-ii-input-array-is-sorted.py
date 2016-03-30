#!/usr/bin/env python
# encoding: utf-8

"""
two-sum-ii-input-array-is-sorted.py
 
Created by Shuailong on 2016-03-30.

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/.

"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            t = target - numbers[i]
            l = i+1
            r = len(numbers)-1
            while l <= r:
                m = (l+r)/2
                if t == numbers[m]:
                    return [i+1, m+1]
                elif t < numbers[m]:
                    r = m-1
                else:
                    l = m+1
        return []

def main():
    solution = Solution()
    numbers = [5, 25, 75]
    target = 100
    print solution.twoSum(numbers, target)
    
if __name__ == '__main__':
    main()

        