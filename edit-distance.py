#!/usr/bin/env python
# encoding: utf-8

"""
edit-distance.py
 
Created by Shuailong on 2015-11-28.

https://leetcode.com/problems/edit-distance/.

"""

'''NOT CORRECT'''

class Solution(object):

    def lcs_length(self, X, Y):
        m = len(X)
        n = len(Y)
        b = [[0 for x in range(n+1)] for x in range(m+1)]
        c = [[0 for x in range(n+1)] for x in range(m+1)]

        for i in range(1, m+1):
            c[i][0] = 0
        for j in range(0, n+1):
            c[0][j] = 0
        for i in range(0, m):
            for j in range(0, n):
                if X[i] == Y[j]:
                    c[i+1][j+1] = c[i][j]+1
                    b[i+1][j+1] = 2 # \
                elif c[i][j+1] >= c[i+1][j]:
                    c[i+1][j+1] = c[i][j+1]
                    b[i+1][j+1] = 1 # |
                else:
                    c[i+1][j+1] = c[i+1][j]
                    b[i+1][j+1] = 0 # -
        return c[m][n]

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lcs = self.lcs_length(word1, word2)
        return max(abs(len(word1) - lcs), abs(len(word2) - lcs))
        


def main():
    word1 = ""
    word2 = "a"
    solution = Solution()
    print solution.minDistance(word1, word2)
    
if __name__ == '__main__':
    main()

