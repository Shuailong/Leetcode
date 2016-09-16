#!/usr/bin/env python
# encoding: utf-8

"""
line-reflection.py

Created by Shuailong on 2016-09-14.

https://leetcode.com/problems/line-reflection/.

"""


class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        xs = [point[0] for point in points]
        line2 = min(xs) + max(xs)

        d = {}
        for point in points:
            d[(point[0], point[1])] = True
        for point in points:
            if (line2-point[0], point[1]) not in d:
                return False
        return True


def main():
    solution = Solution()
    points = [[1, 1], [-1, 1]]
    print solution.isReflected(points)
    points = [[1, 1], [-1, -1]]
    print solution.isReflected(points)


if __name__ == '__main__':
    main()
