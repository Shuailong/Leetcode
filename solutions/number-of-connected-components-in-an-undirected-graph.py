#!/usr/bin/env python
# encoding: utf-8

"""
number-of-connected-components-in-an-undirected-graph.py
 
Created by Shuailong on 2016-03-31.

https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/.

"""

'''Too slow. Improve it later.'''

def MakeSet(n):
    return [[i] for i in range(n)]

def Union(sets, label1, label2):
    s1_idx = 0
    s2_idx = 0
    for i in range(len(sets)):
        if sets[i][0] == label1:
            s1_idx = i
        elif sets[i][0] == label2:
            s2_idx = i
    if len(sets[s1_idx]) > len(sets[s2_idx]):
        sets[s1_idx] += sets[s2_idx]
        sets.remove(sets[s2_idx])
    else:
        sets[s2_idx] += sets[s1_idx]
        sets.remove(sets[s1_idx])
        

def Find(sets, x):
    for s in sets:
        if x in s:
            return s[0]
    
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        sets = MakeSet(n)
        for edge in edges:
            label1 = Find(sets, edge[0])
            label2 = Find(sets, edge[1])
            if label1 != label2:
                Union(sets, label1, label2)
        res = len([s for s in sets if len(s) > 0 ])
        return res
        
def main():
    solution = Solution()
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    print solution.countComponents(n, edges) # 2
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    print solution.countComponents(n,edges) # 1
    
if __name__ == '__main__':
    main()

