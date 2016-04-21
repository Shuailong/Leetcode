#!/usr/bin/env python
# encoding: utf-8

"""
power-of-four.py

Created by Shuailong on 2016-04-21.

https://leetcode.com/problems/power-of-four/.

"""


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num in {
            1,
            4,
            16,
            64,
            256,
            1024,
            4096,
            16384,
            65536,
            262144,
            1048576,
            4194304,
            16777216,
            67108864,
            268435456,
            1073741824
            }


def main():
    # max int: 2**31-1:
    solution = Solution()
    print solution.isPowerOfFour(8)

if __name__ == '__main__':
    main()
