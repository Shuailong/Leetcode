#!/usr/bin/env python
# encoding: utf-8

"""
isomorphic-strings.py
 
Created by Shuailong on 2016-03-03.

https://leetcode.com/problems/isomorphic-strings/.

"""

class Solution(object):
    def getFingerprint(self, s):
        '''
        :type s: str
        :rtype: string
        '''
        d = {}
        key = 0
        fingerprint = ''
        for i in range(len(s)):
            if not d.has_key(s[i]):
                d[s[i]] = str(key)
                key += 1
            fingerprint += d[s[i]]
        return fingerprint


    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if self.getFingerprint(s) == self.getFingerprint(t):
            return True
        else:
            return False


def main():
    solution = Solution()
    s = 'egg'
    t = 'add'
    print solution.isIsomorphic(s, t)
    s = 'foo'
    t = 'bar'
    print solution.isIsomorphic(s, t)
    s = 'paper'
    t = 'title'
    print solution.isIsomorphic(s, t)
    
if __name__ == '__main__':
    main()

