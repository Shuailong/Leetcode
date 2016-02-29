#!/usr/bin/env python
# encoding: utf-8

"""
implement-queue-using-stacks.py
 
Created by Shuailong on 2016-02-17.

https://leetcode.com/problems/implement-queue-using-stacks/.

"""

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        # Using List to implement stack.
        # push = list.append()
        # pop = list.pop()
        # peek = list[-1]
        # size = len(list)
        # isempty = list
        self.s1 = []
        self.s2 = []

    def __repr__(self):
        s = ''
        for element in self.s1:
            s += str(element) + ' '
        return s


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s1.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        

    def peek(self):
        """
        :rtype: int
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        res = self.s2[-1]
        while self.s2:
            self.s1.append(self.s2.pop())
        return res

        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.s1) == 0:
            return True
        else:
            return False

def main():
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print queue
    queue.pop()
    print queue
    print queue.empty()
    print queue.peek()
    queue.pop()
    queue.pop()
    print queue.empty()
    
if __name__ == '__main__':
    main()

        