#!/usr/bin/env python
# encoding: utf-8

"""
design-phone-directory.py

Created by Shuailong on 2016-09-16.

https://leetcode.com/problems/design-phone-directory/.

"""


# Use set


class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.maxNumbers = maxNumbers
        self.pool = [True]*maxNumbers  # number pool
        self.firstUnused = 0  # indicate the next avaible number

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        res = self.firstUnused
        if self.firstUnused != -1:
            self.pool[self.firstUnused] = False
            full = True
            # for i in range(self.firstUnused+1, self.maxNumbers):
            #     if self.pool[i]:
            #         full = False
            #         self.firstUnused = i
            #         break
            # if full:
            #     for i in range(self.firstUnused):
            #         if self.pool[i]:
            #             full = False
            #             self.firstUnused = i
            #         break
            for i in range(self.maxNumbers):
                if self.pool[i]:
                    full = False
                    self.firstUnused = i
                    break
            if full:
                self.firstUnused = -1
        # print self.pool
        return res

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number >= 0 and number < self.maxNumbers and self.pool[number]

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        self.pool[number] = True
        if self.firstUnused == -1:
            self.firstUnused = number


def main():
    maxNumbers = 3
    directory = PhoneDirectory(maxNumbers)
    print directory.get()  # 0
    print directory.get()  # 1
    print directory.check(2)  # True
    print directory.get()  # 2
    print directory.check(2)  # False
    directory.release(2)
    print directory.check(2)  # True
    print directory.get()  # 2
    print directory.check(2)  # False


if __name__ == '__main__':
    main()
