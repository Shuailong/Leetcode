#!/usr/bin/env python
# encoding: utf-8

"""
shortest-word-distance-iii.py
 
Created by Shuailong on 2016-03-30.

https://leetcode.com/problems/shortest-word-distance-iii/.

"""

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1 = []
        idx2 = []
        for i in range(len(words)):
            if words[i] == word1:
                idx1.append(i)
            if words[i] == word2:
                idx2.append(i)
        dist = len(words)
        for i in idx1:
            for j in idx2:
                if i != j:
                    if abs(i - j) == 1:
                        return 1
                    if abs(i - j) < dist:
                        dist = abs(i-j)
        return dist
        

def main():
    solution = Solution()
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = 'makes'
    word2 = 'coding'
    print solution.shortestWordDistance(words,word1,word2)
    word1 = 'makes'
    word2 = 'makes'
    print solution.shortestWordDistance(words,word1,word2)    
    
if __name__ == '__main__':
    main()

        