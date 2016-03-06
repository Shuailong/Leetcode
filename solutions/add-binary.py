#!/usr/bin/env python
# encoding: utf-8

"""
add-binary.py
 
Created by Shuailong on 2016-03-06.

https://leetcode.com/problems/add-binary/.

"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            t = a
            a = b
            b = t

        res = ''
        i = len(a)-1
        j = len(b)-1
        carry = 0
        while i >= 0 and j >= 0:
            d1 = ord(a[i]) - ord('0')
            d2 = ord(b[j]) - ord('0')
            d = (d1 + d2 + carry) & 1
            carry = (d1 + d2 + carry) >> 1
            res = str(d) + res
            i -= 1
            j -= 1

        while i >= 0:
            d1 = ord(a[i]) - ord('0')
            d = (d1 + carry) & 1
            carry = (d1 + carry) >> 1
            res = str(d) + res
            i -= 1
        if carry:
            res = str(carry) + res

        return res
        

def main():
    solution = Solution()
    a = '110010'
    b = '10111'
    print solution.addBinary(a, b)
    
if __name__ == '__main__':
    main()

