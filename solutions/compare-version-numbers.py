#!/usr/bin/env python
# encoding: utf-8

"""
compare-version-numbers.py
 
Created by Shuailong on 2016-03-15.

https://leetcode.com/problems/compare-version-numbers/.

"""

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        seglist1 = map(int, version1.split('.'))
        seglist2 = map(int, version2.split('.'))

        if len(seglist1) < len(seglist2):
            seglist1.extend([0]*(len(seglist2) - len(seglist1)))
        else:
            seglist2.extend([0]*(len(seglist1) - len(seglist2)))

        return cmp(seglist1, seglist2)

def main():
    solution = Solution()
    version1 = '0.1'
    version2 = '1.1'
    version3 = '1.2'
    version4 = '13.37'
    print  solution.compareVersion(version1, version2)
    print  solution.compareVersion(version2, version3)
    print  solution.compareVersion(version3, version4)

    print  solution.compareVersion('1.0.0', '1')

if __name__ == '__main__':
    main()

        