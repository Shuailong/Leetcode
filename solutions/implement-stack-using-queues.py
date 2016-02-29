#!/usr/bin/env python
# encoding: utf-8

"""
implement-stack-using-queues.py
 
Created by Shuailong on 2016-02-22.

https://leetcode.com/problems/implement-stack-using-queues/.

"""

from collections import deque

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        # Using deque to implement queue.
        # push = deque.append()
        # pop = deque.popleft()
        # peek = deque[-1]
        # size = len(deque)
        # isempty = deque
        self.q1 = deque()
        self.q2 = deque()

    def __repr__(self):
        s = '['
        for element in self.q1:
            s += str(element) + ' '
        s += ']'
        s += ' ['
        for element in self.q2:
            s += str(element) + ' '
        s += ']'
        return s



    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q1.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())
        self.q1.popleft()
        while self.q2:
            self.q1.append(self.q2.popleft())


    def top(self):
        """
        :rtype: int
        """
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())
        res = self.q1.popleft()
        while self.q2:
            self.q1.append(self.q2.popleft())
        self.q1.append(res)

        return res

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q1) == 0
        

def main():
    stack = Stack()
    print stack.empty()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print stack
    print stack.top()
    print stack
    print stack.empty()
    stack.pop()
    print stack
    stack.pop()
    print stack.top()
    stack.pop()
    print stack.empty()
    
if __name__ == '__main__':
    main()

        