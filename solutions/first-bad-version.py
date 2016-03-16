#!/usr/bin/env python
# encoding: utf-8

"""
first-bad-version.py
 
Created by Shuailong on 2016-03-16.

https://leetcode.com/problems/first-bad-version/.

"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool

def isBadVersion(version):
    return version >= 10

class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l <= r:
            m = (l+r)/2
            if isBadVersion(m) and not isBadVersion(m-1):
                return m
            elif isBadVersion(m) and isBadVersion(m-1):
                r = m-1
            elif not isBadVersion(m) and not isBadVersion(m-1):
                l = m+1

        

def main():
    solution = Solution()
    n = 1000
    print solution.firstBadVersion(n)
    
if __name__ == '__main__':
    main()

        