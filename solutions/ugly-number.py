#!/usr/bin/env python
# encoding: utf-8

"""
ugly-number.py
 
Created by Shuailong on 2016-02-03.

https://leetcode.com/problems/ugly-number/.

"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # if num == 1:
        #     return True
        if num <= 0:
            return False
        while num != 1:
            flag = False
            if num % 2 == 0:
                num /= 2
                flag = True
            if num % 3 == 0:
                num /= 3
                flag = True
            if num % 5 == 0:
                num /= 5
                flag = True
            if not flag:
                return False
        return True

        
def main():
    solution = Solution()
    num = 1
    print solution.isUgly(num)
    num = 8
    print solution.isUgly(num)
    num = 147
    print solution.isUgly(num)
    
if __name__ == '__main__':
    main()

