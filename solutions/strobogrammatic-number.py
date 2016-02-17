#!/usr/bin/env python
# encoding: utf-8

"""
strobogrammatic-number.py
 
Created by Shuailong on 2016-02-17.

https://leetcode.com/problems/strobogrammatic-number/.

"""

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """

        illegal = ['2','3','4','5','7']
        for digit in illegal:
            if digit in num:
                return False
        rdigits = list(reversed(num))
        for i in range(len(num)):
            if num[i] != rdigits[i]:
                if num[i] == '6' and rdigits[i] == '9' or num[i] == '9' and rdigits[i] == '6':
                    continue
                else:
                    return False
            else:
                if num[i] == '6' or num[i] == '9':
                    return False
        return True



def main():
    solution = Solution()
    num = '6'
    print solution.isStrobogrammatic(num)
    num = '619'
    print solution.isStrobogrammatic(num)
    num = '818'
    print solution.isStrobogrammatic(num)
    
if __name__ == '__main__':
    main()

        