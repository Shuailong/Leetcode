#!/usr/bin/env python
# encoding: utf-8

"""
happy-number.py
 
Created by Shuailong on 2016-02-05.

https://leetcode.com/problems/happy-number/.

"""

class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = {}
        count[n] = 1
        while n != 1:
            nn = n
            n = 0
            while nn != 0:
                n += (nn % 10)*(nn % 10)
                nn /= 10
            if count.get(n,0) == 0:
                count[n] = 1
            else:
                count[n] += 1
            if count[n] > 1:
                return False

        return True
        

def main():
    solution = Solution()
    print solution.isHappy(199)
    
if __name__ == '__main__':
    main()

