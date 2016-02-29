#!/usr/bin/env python
# encoding: utf-8

"""
reverse-integer.py
 
Created by Shuailong on 2016-01-15.

https://leetcode.com/problems/reverse-integer/.

"""

'''
Note1: Python sys.maxint = 2**64-1
Note2: Solution and Solution1 are both accepted. Solution is quicker.

'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
        	x = -x
        	neg = True

        s = str(x)[::-1]

        if neg:
        	s = '-' + s

        s = int(s)
        MAX = 2**31-1
        if s > MAX or s < -MAX:
        	return 0
        
        return s

class Solution1(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX = 2**31-1
        res = 0
        neg = False
        if x < 0:
        	x  = -x
        	neg = True
        while x != 0:
        	res = res * 10 + x % 10
        	x /= 10
        if neg:
        	res = -res
        if res > MAX or res < -MAX-1:
        	return 0
        
        return res

        
def main():
    solution = Solution()
 
    print solution.reverse(-123456789)
    
if __name__ == '__main__':
    main()

        