#!/usr/bin/env python
# encoding: utf-8

"""
valid-word-square.py

Created by Shuailong on 2016-10-19.

https://leetcode.com/problems/valid-word-square/.

"""


class Solution(object):
    def transpose(self, words):
        max_len = len(words[0])
        words_t = ['']*max_len
        for i in range(0, max_len):
            words_t[i] = ''
            for word in words:
                if i < len(word):
                    words_t[i] += word[i]
        return words_t

    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        words_t = self.transpose(words)
        if len(words) != len(words_t):
            return False
        for i in range(len(words)):
            if words[i] != words_t[i]:
                return False
        return True

    def validWordSquare2(self, words):
        word_mat = [list(word) for word in words]
        for word in word_mat:
            word += [None]*(len(words[0])-len(word))
        word_tra = [list(i) for i in map(None, *word_mat)]
        return word_mat == word_tra


def main():
    solution = Solution()
    words = [
        "abcd",
        "bnrt",
        "crmy",
        "dtye"
        ]
    print solution.validWordSquare2(words)

    words = [
        "abcd",
        "bnrt",
        "crm",
        "dt"
        ]

    print solution.validWordSquare2(words)

    words = [
        "ball",
        "area",
        "read",
        "lady"
        ]
    print solution.validWordSquare2(words)


if __name__ == '__main__':
    main()
