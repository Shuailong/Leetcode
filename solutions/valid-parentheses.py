#!/usr/bin/env python
# encoding: utf-8

"""
valid-parentheses.py
 
Created by Shuailong on 2016-01-15.

https://leetcode.com/problems/valid-parentheses/.

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if s[i] == ')':
                    if len(stack) == 0:
                        return False
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif s[i] == ']':
                    if len(stack) == 0:
                        return False
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif s[i] == '}':
                    if len(stack) == 0:
                        return False
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        if len(stack) > 0:
            return False

        return True



def main():
    solution = Solution()
    print solution.isValid('()[]{}') == True
    print solution.isValid('([)]') == False
    print solution.isValid('()') == True
    print solution.isValid('(]') == False
    
if __name__ == '__main__':
    main()

