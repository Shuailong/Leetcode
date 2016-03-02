#!/usr/bin/env python
# encoding: utf-8

"""
reverse-bits.py
 
Created by Shuailong on 2016-03-02.

https://leetcode.com/problems/reverse-bits/.

"""

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        count = 0
        while n:
            d = n & 1
            n >>= 1
            res <<= 1
            res += d
            count += 1
        res <<= 32-count

        return res

def main():
    solution = Solution()
    n = 43261596
    print solution.reverseBits(n)
    
if __name__ == '__main__':
    main()

        