#!/usr/bin/env python
# encoding: utf-8

"""
palindrome-number.py
 
Created by Shuailong on 2016-01-15.

https://leetcode.com/problems/palindrome-number/.

"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        xx = x
        reverse = 0
        while x != 0:
            reverse = reverse * 10 + x % 10
            x /= 10
        if reverse == xx:
            return True
        else:
            return False
        


class Solution1(object):
    '''Do use extra space'''
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        l = len(s)
        for i in range(l/2):
            if s[i] != s[l-1-i]:
                return False
        return True

def main():
    solution = Solution()
    print solution.isPalindrome(1)
    
if __name__ == '__main__':
    main()

