#!/usr/bin/env python
# encoding: utf-8

"""
meeting-rooms.py
 
Created by Shuailong on 2016-02-04.

https://leetcode.com/problems/meeting-rooms/.

"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '[' + str(self.start) + ', ' + str(self.end) + ']'

class Solution(object):

    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda interval: interval.start)
        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True
        
    
def main():
    solution = Solution()
    intervals = []
    intervals.append(Interval(15,20))
    intervals.append(Interval(0,30))
    intervals.append(Interval(5,10))
    

    print solution.canAttendMeetings(intervals)
    
if __name__ == '__main__':
    main()

