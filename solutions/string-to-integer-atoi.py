#!/usr/bin/env python
# encoding: utf-8

"""
string-to-integer-atoi.py
 
Created by Shuailong on 2016-01-15.

https://leetcode.com/problems/string-to-integer-atoi/.

"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) < 1:
            return 0

        str = str.strip()
        
        str_valid = ''
        for i in range(len(str)):
            if str[i] not in '01234567890':
                if i == 0 and (str[i] == '-' or str[i] == '+') and len(str) > 1:
                    str_valid += str[i]
                    continue
                else:
                    break
            else:
                str_valid += str[i]

        if len(str_valid) == 1 and (str_valid == '+' or str_valid == '-') or len(str_valid) == 0:
            return 0

        res = int(str_valid)
        MAX = 2**31-1

        if res > MAX:
            return MAX
        if res < -MAX-1:
            return -MAX-1
        return res


def main():
    solution = Solution()
    print solution.myAtoi("-2147483648")
    
if __name__ == '__main__':
    main()

