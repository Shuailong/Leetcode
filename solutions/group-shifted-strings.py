#!/usr/bin/env python
# encoding: utf-8

"""
group-shifted-strings.py
 
Created by Shuailong on 2016-02-24.

https://leetcode.com/problems/group-shifted-strings/.

"""

class Solution(object):
    def diff(self, a, b):
        """
        :type a: char
        :type b: char
        :rtype: int
        """
        difference = ord(b) - ord(a)
        if difference < 0:
            difference += 26
        return difference

    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for string in strings:
            key = ''
            if len(string) == 1:
                key = 's'
            else:
                for i in range(1, len(string)):
                    key += str(self.diff(string[i-1], string[i]))+'-'
            if d.get(key, 0) == 0:
                d[key] = [string]
            else:
                d[key].append(string)
        res = d.values()
        for l in res:
            l.sort()
        return res



        

def main():
    strings = ["xyz", "bcd", "acef", "abc", "az", "ba", "a", "z"]
    solution = Solution()
    print solution.groupStrings(strings)
    
if __name__ == '__main__':
    main()

