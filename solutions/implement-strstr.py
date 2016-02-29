#!/usr/bin/env python
# encoding: utf-8

"""
implement-strstr.py
 
Created by Shuailong on 2016-01-16.

https://leetcode.com/problems/implement-strstr/.

"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        for start_index in range(len(haystack)-len(needle)+1):
            matched_len = 0
            i = start_index
            for j in range(len(needle)):
                if haystack[i] == needle[j]:
                    matched_len += 1
                i += 1
            if matched_len == len(needle):
                return start_index
        return -1

        

def main():
    solution = Solution()
    haystack = '1'
    needle = '1'

    print solution.strStr(haystack, needle)
    
if __name__ == '__main__':
    main()

        