#!/usr/bin/env python
# encoding: utf-8

"""
read-n-characters-given-read4.py
 
Created by Shuailong on 2016-03-17.

https://leetcode.com/problems/read-n-characters-given-read4/.

"""

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0 # index of current buf position
        while n > 0: # there are n characters to read
            buf4 = ['']*4
            l = read4(buf4)
            if not l:
                return i
            valid = min(l, n)
            buf[i:i+valid] = buf4[:valid]
            n -= valid
            i += valid
        return i



def main():
    pass
    
if __name__ == '__main__':
    main()

