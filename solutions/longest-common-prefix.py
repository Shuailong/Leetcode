#!/usr/bin/env python
# encoding: utf-8

"""
longest-common-prefix.py
 
Created by Shuailong on 2016-01-15.

https://leetcode.com/problems/longest-common-prefix/.

"""

class Solution(object):
    def commonPrefix(self, str1, str2):
        res = ''
        i = 0
        while i < len(str1) and i < len(str2):
            if str1[i] == str2[i]:
                res += str1[i]
            else:
                break
            i += 1
        return res

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1:
            return ''
        res = strs[0]
        for str in strs:
            res = self.commonPrefix(str, res)
        return res


def main():
    solution = Solution()
    strs = ['abcef','abcedsdfafasdf','abced']
    print solution.longestCommonPrefix(strs)
    
if __name__ == '__main__':
    main()

        