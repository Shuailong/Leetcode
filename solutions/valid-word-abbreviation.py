#!/usr/bin/env python
# encoding: utf-8

"""
valid-word-abbreviation.py

Created by Shuailong on 2016-10-19.

https://leetcode.com/problems/valid-word-abbreviation/.

"""


class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = 0
        first = True
        num = ''
        for j in range(len(abbr)):
            c = abbr[j]
            if c.isalpha():
                if num:
                    i += int(num)
                    if i >= len(word):
                        return False
                    num = ''
                if word[i] == c:
                    i += 1
                else:
                    return False

            elif c.isdigit():
                if c == '0':
                    if not (j > 0 and abbr[j-1].isdigit()):
                        return False

                if first:
                    num = c
                    first = False
                else:
                    num += c
            else:
                return False

        if num and int(num) != len(word)-i:
            return False

        return True


def main():
    solution = Solution()

    s = "internationalization"
    abbr = "i12iz4n"
    print solution.validWordAbbreviation(s, abbr)

    s = "a"
    abbr = "01"
    print solution.validWordAbbreviation(s, abbr)


if __name__ == '__main__':
    main()
