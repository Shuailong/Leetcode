#!/usr/bin/env python
# encoding: utf-8

"""
flip-game.py
 
Created by Shuailong on 2016-01-05.

https://leetcode.com/problems/flip-game/.

"""

class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        for i in xrange(len(s)-1):
            if s[i:i+2] == '++':
                ret.append(s[:i] + '--' + s[i+2:])
        return ret

def main():
    solution = Solution()
    print solution.generatePossibleNextMoves('++++')
    
if __name__ == '__main__':
    main()

