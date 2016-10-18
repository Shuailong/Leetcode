#!/usr/bin/env python
# encoding: utf-8

"""
fizz-buzz.py

Created by Shuailong on 2016-10-18.

https://leetcode.com/problems/fizz-buzz/.

"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 != 0:
                res.append('Fizz')
            elif i % 5 == 0 and i % 3 != 0:
                res.append('Buzz')
            elif i % 15 == 0:
                res.append('FizzBuzz')
            else:
                res.append(str(i))
        return res


def main():
    solution = Solution()
    print solution.fizzBuzz(15)

if __name__ == '__main__':
    main()
