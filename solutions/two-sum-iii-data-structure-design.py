#!/usr/bin/env python
# encoding: utf-8

"""
two-sum-iii-data-structure-design.py
 
Created by Shuailong on 2016-03-07.

https://leetcode.com/problems/two-sum-iii-data-structure-design/.

"""

class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.d = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.d:
            self.d[number] += 1
        else:
            self.d[number] = 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.d:
            diff = value - num
            if diff == num and self.d[num] > 1 or diff != num and diff in self.d:
                return True
        return False

        

def main():
    twoSum = TwoSum()
    twoSum.add(1)
    twoSum.add(3)
    twoSum.add(5)
    print twoSum.find(4)
    print twoSum.find(7)
        
if __name__ == '__main__':
    main()

        