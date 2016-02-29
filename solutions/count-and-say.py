#!/usr/bin/env python
# encoding: utf-8

"""
count-and-say.py
 
Created by Shuailong on 2016-01-16.

https://leetcode.com/problems/count-and-say/.

"""

class Solution(object):
    def count(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = ''
        p = 0
        while p < len(s):
            c = s[p]
            count = 0
            while p < len(s) and s[p] == c:
                p += 1
                count += 1
            res += str(count) + c
        return res


    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        s = '1'
        for i in range(n-1):
            s = self.count(s)
        return s

def main():
    solution = Solution()
    n = 1
    print solution.countAndSay(n)
    
if __name__ == '__main__':
    main()

