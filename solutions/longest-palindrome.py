#!/usr/bin/env python
# encoding: utf-8

"""
longest-palindrome.py

Created by Shuailong on 2016-10-18.

https://leetcode.com/problems/longest-palindrome/.

"""


from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        c = Counter(s)
        flag = False
        for ch in c:
            if c[ch] % 2 == 0:
                res += c[ch]
            if c[ch] % 2 == 1:
                flag = True
                res += c[ch]-1
        if flag:
            res += 1

        return res


def main():
    solution = Solution()
    s = 'abccccdd'
    s = 'civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'
    print solution.longestPalindrome(s)

if __name__ == '__main__':
    main()
