#!/usr/bin/env python
# encoding: utf-8

"""
power-of-two.py
 
Created by Shuailong on 2016-02-13.

https://leetcode.com/problems/power-of-two/.

"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        count = 0
        while n != 0:
            bit = n & 1
            if bit == 1:
                count += 1
            n >>= 1
        if count == 1:
            return True
        else:
            return False
        

def main():
    solution = Solution()
    n = -16
    print solution.isPowerOfTwo(n)
    
if __name__ == '__main__':
    main()

        