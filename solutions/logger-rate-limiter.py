#!/usr/bin/env python
# encoding: utf-8

"""
logger-rate-limiter.py

Created by Shuailong on 2016-07-25.

https://leetcode.com/problems/logger-rate-limiter/.

"""


class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._d = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """

        if message in self._d and timestamp - self._d[message] < 10:
            return False
        else:
            self._d[message] = timestamp
            return True


def main():
    logger = Logger()

    #logging string "foo" at timestamp 1
    print logger.shouldPrintMessage(1, "foo")  # returns true

    #logging string "bar" at timestamp 2
    print logger.shouldPrintMessage(2, "bar")  # returns true

    #logging string "foo" at timestamp 3
    print logger.shouldPrintMessage(3, "foo")  # returns false

    #logging string "bar" at timestamp 8
    print logger.shouldPrintMessage(8, "bar")  # returns false

    #logging string "foo" at timestamp 10
    print logger.shouldPrintMessage(10, "foo")  # returns false

    #logging string "foo" at timestamp 11
    print logger.shouldPrintMessage(11, "foo")  # returns true

if __name__ == '__main__':
    main()
