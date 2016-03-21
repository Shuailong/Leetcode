#!/usr/bin/env python
# encoding: utf-8

"""
count-primes.py
 
Created by Shuailong on 2016-03-18.

https://leetcode.com/problems/count-primes/.

"""

from math import sqrt
class Solution1(object):
    def isPrime(self, num):
        if num < 2:
            return False
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                return False
        return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(n):
            if self.isPrime(i):
                res += 1
        return res

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [True]*(n)  # use isPrime[1] to isPrime[n]
        p = 2
        while p*p < n:
            if isPrime[p]:
                i = p**2
                while i < n:
                    isPrime[i] = False
                    i += p
            p += 1
        return isPrime[2:].count(True)

def main():
    solution = Solution()
    n = 120
    print solution.countPrimes(n)
    
if __name__ == '__main__':
    main()

