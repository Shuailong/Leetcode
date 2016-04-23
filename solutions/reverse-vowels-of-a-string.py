#!/usr/bin/env python
# encoding: utf-8

"""
reverse-vowels-of-a-string.py

Created by Shuailong on 2016-04-23.

https://leetcode.com/problems/reverse-vowels-of-a-string/.

"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWEL = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        vowels = []
        res = list(s)
        for i in range(len(s)):
            if s[i] in VOWEL:
                vowels.append(s[i])

        j = 0
        for i in range(len(s)-1, -1, -1):
            if res[i] in VOWEL:
                res[i] = vowels[j]
                j += 1

        return ''.join(res)


def main():
    solution = Solution()
    s = "leetcode"
    print solution.reverseVowels(s)



if __name__ == '__main__':
    main()
