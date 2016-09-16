#!/usr/bin/env python
# encoding: utf-8

"""
integer-replacement.py

Created by Shuailong on 2016-09-14.

https://leetcode.com/problems/integer-replacement/.

"""


memo = {}


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        global memo
        if n in memo:
            return memo[n]

        if n == 1:
            return 0
        if n % 2 == 0:
            memo[n] = 1 + self.integerReplacement(n/2)
            return memo[n]
        else:
            memo[n] = 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))
            return memo[n]


def main():
    solution = Solution()
    print solution.integerReplacement(65535)


if __name__ == '__main__':
    main()
