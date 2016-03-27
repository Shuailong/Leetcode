#!/usr/bin/env python
# encoding: utf-8

"""
sparse-matrix-multiplication.py
 
Created by Shuailong on 2016-03-27.

https://leetcode.com/problems/sparse-matrix-multiplication/.

"""

'''Passed in 280ms. Think about using any() to speed up.'''

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        # A: m*n  B: n*p
        m = len(A)
        n = len(A[0])
        p = len(B[0])

        # A*B: m*p
        AB = [[0 for col in range(p)] for row in range(m)]

        A_row_indices = {}
        for i in range(m):
            for j in range(n):
                if A[i][j]:
                    if j not in A_row_indices:
                        A_row_indices[j] = [i]
                    else:
                        A_row_indices[j].append(i)

        B_col_indices = {}
        for i in range(n):
            for j in range(p):
                if B[i][j]:
                    if i not in B_col_indices:
                        B_col_indices[i] = [j]
                    else:
                        B_col_indices[i].append(j)

        common_keys = set(A_row_indices.keys()) & set(B_col_indices.keys())

        for k in common_keys:
            for i in A_row_indices[k]:
                for j in B_col_indices[k]:
                    AB[i][j] += A[i][k]*B[k][j]

        return AB

def main():
    solution = Solution()
    A = [
          [ 1, 0, 0],
          [-1, 0, 3]
        ]

    B = [
          [ 7, 0, 0 ],
          [ 0, 0, 0 ],
          [ 0, 0, 1 ]
        ]

    print solution.multiply(A, B)

    
if __name__ == '__main__':
    main()

