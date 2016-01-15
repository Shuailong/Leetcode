#!/usr/bin/env python
# encoding: utf-8

"""
power-of-three.py
 
Created by Shuailong on 2016-01-10.

https://leetcode.com/problems/power-of-three/.

"""

'''Refer to some discussions. Think about it later. '''

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n in {1,
                3,
                9,
                27,
                81,
                243,
                729,
                2187,
                6561,
                19683,
                59049,
                177147,
                531441,
                1594323,
                4782969,
                14348907,
                43046721,
                129140163,
                387420489,
                1162261467,
                3486784401,
                10460353203,
                31381059609,
                94143178827,
                282429536481,
                847288609443,
                2541865828329,
                7625597484987,
                22876792454961,
                68630377364883,
                205891132094649,
                617673396283947,
                1853020188851841,
                5559060566555523,
                16677181699666569,
                50031545098999707,
                150094635296999121,
                450283905890997363,
                1350851717672992089,
                4052555153018976267,
                12157665459056928801,
            }
        

def main():
    n = 243
    solution = Solution()
    print solution.isPowerOfThree(n)
    
if __name__ == '__main__':
    main()

        