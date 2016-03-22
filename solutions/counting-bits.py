#!/usr/bin/env python
# encoding: utf-8

"""
counting-bits.py
 
Created by Shuailong on 2016-03-22.

https://leetcode.com/problems/counting-bits/.

"""
class Solution(object):
    def countBits(self, num):
        """
        Think about its nature. In recursive way.

        :type num: int
        :rtype: List[int]
        """
        res = [0]*(num+1)
        for i in range(1, num+1):
            res[i] = res[i/2] + (i&1) 
        return res
        
class Solution2(object):
    def countBits(self, num):
        """
        Find the regular patterns between difference of numbers.

        :type num: int
        :rtype: List[int]
        """
        res = [0]*(num+1)
        for i in range(1, num+1):
            ii = i
            trailing_zeros = 0
            while ii != 0:
                if ii & 1 == 1:
                    break
                trailing_zeros += 1
                ii >>= 1
            res[i] = res[i-1] - (trailing_zeros-1) 
        return res


class Solution1(object):
    '''
    Naive method
    '''
    def count(self, num):
        c = 0
        while num != 0:
            c += num & 1
            num >>= 1

        return c

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]*(num+1)
        for i in range(1, num+1):
            res[i] = self.count(i)
        return res


def main():
    solution = Solution()
    num = 100
    print solution.countBits(num)
    
if __name__ == '__main__':
    main()

