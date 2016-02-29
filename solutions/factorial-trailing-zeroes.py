#!/usr/bin/env python
# encoding: utf-8

"""
factorial-trailing-zeroes.py
 
Created by Shuailong on 2016-02-21.

https://leetcode.com/problems/factorial-trailing-zeroes/.

"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        max_iter = 15  # 5**14 > max_int
        for fact in range(1, max_iter):
            count += n / 5 ** fact

        return count
        
        


def main():
    solution = Solution()
    n = 25
    for n in range(1, 100):
        print solution.trailingZeroes2(n), solution.trailingZeroes(n)

    
if __name__ == '__main__':
    main()

