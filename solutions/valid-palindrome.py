#!/usr/bin/env python
# encoding: utf-8

"""
valid-palindrome.py
 
Created by Shuailong on 2016-03-09.

https://leetcode.com/problems/valid-palindrome/.

"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1
        while i <= j:
            while i <= j-1 and not s[i].isalnum():
                i += 1
            while i <= j-1 and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True
        

def main():
    solution = Solution()
    print solution.isPalindrome('A man, a plan, a canal: Panama')
    print solution.isPalindrome('race a car')
    print solution.isPalindrome(' ')
    
if __name__ == '__main__':
    main()

        