#!/usr/bin/env python
# encoding: utf-8

"""
guess-number-higher-or-lower.py

Created by Shuailong on 2016-07-25.

https://leetcode.com/problems/guess-number-higher-or-lower/.

"""

'''
Note: read the problem carefully.
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0


def guess(num):
    real = 6
    if num == real:
        return 0
    elif num < real:
        return -1
    else:
        return 1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n

        while l <= h:
            m = (l+h)/2
            if guess(m) == 0:
                return m
            elif guess(m) == -1:
                h = m-1
            else:
                l = m+1



def main():
    solution = Solution()
    print solution.guessNumber(10)

if __name__ == '__main__':
    main()
