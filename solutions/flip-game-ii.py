#!/usr/bin/env python
# encoding: utf-8

"""
flip-game-ii.py
 
Created by Shuailong on 2016-01-05.

https://leetcode.com/problems/flip-game-ii/.

"""

class Solution(object):

    def __init__(self):
        self.memo = {}

    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if self.memo.get(s,0) != 0:
            return self.memo[s]

        l = self.generatePossibleNextMoves(s)
        if len(l) == 0:
            self.memo[s] = False
            return False
        for ss in l:
            if not self.canWin(ss):
                self.memo[s] = True
                return True
        self.memo[s] = False
        return False


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
    print solution.canWin("+++++++++++++++++++++")
    
if __name__ == '__main__':
    main()

