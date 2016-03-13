#!/usr/bin/env python
# encoding: utf-8

"""
min-stack.py
 
Created by Shuailong on 2016-03-13.

https://leetcode.com/problems/min-stack/.

"""

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.min_idx = -1
        
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.arr.append(x)
        if self.min_idx == -1 or x < self.arr[self.min_idx]:
            self.min_idx = len(self.arr)-1
        
    def pop(self):
        """
        :rtype: nothing
        """
        if self.min_idx == len(self.arr)-1:
            self.min_idx = 0
            for i in range(1, len(self.arr)-1):
                if self.arr[i] < self.arr[self.min_idx]:
                    self.min_idx = i
        self.arr.pop()    

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        if self.min_idx != -1:
            return self.arr[self.min_idx]
        else:
            return None

def main():
    stack = MinStack()
    stack.push(1)
    stack.top()
    stack.push(2)
    stack.push(3)
    stack.push(-1)
    print stack.getMin(), -1
    print stack.top(), -1
    stack.pop()
    print stack.getMin(), 1
    stack.pop()

    
if __name__ == '__main__':
    main()

        