#!/usr/bin/env python
# encoding: utf-8

"""
rectangle-area.py
 
Created by Shuailong on 2016-02-28.

https://leetcode.com/problems/rectangle-area/.

"""

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        areaA = (C-A)*(D-B)
        areaB = (G-E)*(H-F)
        intersec = 0
        if E > C or A > G or F > D or B > H:
            intersec = 0
        else:
            Xs = [A, C, E, G]
            Xs.sort()
            Ys = [B, D, F, H]
            Ys.sort()
            intersec = (Xs[2]-Xs[1])*(Ys[2]-Ys[1])

        # print areaA, areaB, intersec
        return areaA + areaB - intersec
        
def main():
    solution = Solution()
    A = -3
    B = 0
    C = 3
    D = 4
    E = 0
    F = -1
    G = 9
    H = 2
    # A = 0
    # B = 0
    # C = 0
    # D = 0
    # E = -1
    # F = -1
    # G = 1
    # H = 1
    print solution.computeArea(A, B, C, D, E, F, G, H)
    
if __name__ == '__main__':
    main()

        