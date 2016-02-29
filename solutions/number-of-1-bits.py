#!/usr/bin/env python
# encoding: utf-8

"""
number-of-1-bits.py
 
Created by Shuailong on 2016-02-04.

https://leetcode.com/problems/number-of-1-bits/.

"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count
        

def main():
    solution = Solution()
    print solution.hammingWeight(11)
    
if __name__ == '__main__':
    main()

        