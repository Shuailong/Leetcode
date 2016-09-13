#!/usr/bin/env python
# encoding: utf-8

"""
rotate-function.py

Created by Shuailong on 2016-09-13.

https://leetcode.com/problems/rotate-function/.

"""


class Solution(object):

    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        value = 0
        for i in range(n):
            value += i * A[i]

        max_value = value

        sumA = sum(A)

        for i in range(n):
            value = value + sumA - n*A[n-i-1]
            max_value = max(max_value, value)

        return max_value


def main():
    solution = Solution()
    A = [4, 3, 2, 6]
    print solution.maxRotateFunction(A)


if __name__ == '__main__':
    main()
