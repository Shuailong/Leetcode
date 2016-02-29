#!/usr/bin/env python
# encoding: utf-8

"""
bulb-switcher.py
 
Created by Shuailong on 2015-12-19.

https://leetcode.com/problems/bulb-switcher.

"""

'''key: find the law and rewrite the solution'''

from math import floor,sqrt

class Solution1(object):

    '''Too time consuming'''

    def factors(self,n):
        '''
        How many factors does the integer n have?
        '''
        if n == 1:
            return 1

        count = 0

        for i in range(2, n):
            if n % i == 0:
                count += 1
        return count+2

    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(1, n+1):
            if self.factors(i) % 2 == 1:
                count += 1
        return count

class Solution(object):
    def bulbSwitch(self,n):
        """
        :type n: int
        :rtype: int
        """
        return int(floor(sqrt(n)))
 

def main():
    solution = Solution()
    solution1 = Solution1()

    for n in range(1,20):
        print n, solution.bulbSwitch(n)
    
if __name__ == '__main__':
    main()

        