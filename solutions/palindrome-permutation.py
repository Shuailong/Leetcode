#!/usr/bin/env python
# encoding: utf-8

"""
palindrome-permutation.py
 
Created by Shuailong on 2016-02-04.

https://leetcode.com/problems/palindrome-permutation/.

"""

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = {}
        for i in range(len(s)):
            c = s[i]
            if count.get(c, 0) == 0:
                count[c] = 1
            else:
                count[c] += 1
        odd_count = 0
        for k in count:
            if count[k] % 2 == 1:
                odd_count += 1
        if odd_count > 1:
            return False
        return True
        

def main():
    solution = Solution()
    s = 'aaabbc'
    print solution.canPermutePalindrome(s)
    s = 'aab'
    print solution.canPermutePalindrome(s)
    s = 'carerac'
    print solution.canPermutePalindrome(s)
    
if __name__ == '__main__':
    main()

