#!/usr/bin/env python
# encoding: utf-8

"""
nested-list-weight-sum.py
 
Created by Shuailong on 2016-03-30.

https://leetcode.com/problems/nested-list-weight-sum/.

"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):

#     def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """


#     def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """

#     def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum1(self, nestedList, depth):
        s = 0
        for nl in nestedList:
            if nl.isInteger():
                s += depth * nl.getInteger()
            else:
                s += self.depthSum1(nl.getList(), depth+1)
        return s

    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return self.depthSum1(nestedList, 1)


def main():
    pass
    
if __name__ == '__main__':
    main()

