#!/usr/bin/env python
# encoding: utf-8

"""
add-digits.py
 
Created by Shuailong on 2016-02-04.

https://leetcode.com/problems/add-digits/.

"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = num % 9
        if res == 0 and num != 0:
            return 9
        return res
        

# class Solution(object):
#     def addDigits(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         while num >= 10:
#             num_copy = num
#             num = 0
#             while num_copy != 0:
#                 num += num_copy % 10
#                 num_copy /= 10
#         return num
        

def main():
    solution = Solution()
    for num in range(1, 1000):
        print solution.addDigits(num),
    
if __name__ == '__main__':
    main()

