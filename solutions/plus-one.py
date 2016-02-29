#!/usr/bin/env python
# encoding: utf-8

"""
plus-one.py
 
Created by Shuailong on 2016-02-05.

https://leetcode.com/problems/plus-one/.

"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            d = digits[i]
            digits[i] = (d + carry) % 10
            carry = (d + carry) / 10
        if carry != 0:
            digits.insert(0, carry)
        return digits

def main():
    solution = Solution()
    digits = [9,9,9]
    print solution.plusOne(digits)
    
if __name__ == '__main__':
    main()

        