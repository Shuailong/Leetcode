#!/usr/bin/env python
# encoding: utf-8

"""
moving-average-from-data-stream.py

Created by Shuailong on 2016-05-06.

https://leetcode.com/problems/moving-average-from-data-stream/.

"""


class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.prevs = []
        
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.prevs.insert(0, val)
        if len(self.prevs) <= self.size:
            return float(sum(self.prevs))/len(self.prevs)
        else:
            self.prevs.pop()
            return float(sum(self.prevs))/self.size

def main():
    obj = MovingAverage(3)
    p = obj.next(1)
    print p
    p = obj.next(10)
    print p
    p = obj.next(3)
    print p
    p = obj.next(5)
    print p


if __name__ == '__main__':
    main()
