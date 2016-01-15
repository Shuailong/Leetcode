#!/usr/bin/env python
# encoding: utf-8

"""
nim-game.py
 
Created by Shuailong on 2015-12-21.

https://leetcode.com/problems/nim-game/.

"""

class Solution1(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        '''Too time consuming'''
        win1 = True
        win2 = True
        win3 = True
        win = True
        i = 4
        while i < n+1:
            win = not win1 or not win2 or not win3
            win1 = win2
            win2 = win3
            win3 = win
            i += 1
        return win

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        '''Find the law and rewrite'''

        return n & 3 != 0
        # return n % 4 != 0



def main():
    solution = Solution()
    n = 4
    print solution.canWinNim(n)

    
if __name__ == '__main__':
    main()

        