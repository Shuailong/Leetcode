#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-10-23 14:58:13
# @Last Modified by: Shuailong
# @Last Modified time: 2019-10-23 14:58:17

from typing import List, Tuple

"""
https://leetcode.com/problems/shortest-bridge/
"""


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        def find_any_one(A: List[List[int]]) -> Tuple[int, int]:
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[i][j] == 1:
                        return (i, j)
        start_i, start_j = find_any_one(A)
        seen = set()
        queue = []
        seen.add((start_i, start_j))
        queue.append((start_i, start_j))
        while queue:
            i, j = queue.pop(0)
            neighbors = []
            if i-1 >= 0 and A[i-1][j] == 1:
                neighbors.append((i-1, j))
            if i+1 < len(A) and A[i+1][j] == 1:
                neighbors.append((i+1, j))
            if j-1 >= 0 and A[i][j-1] == 1:
                neighbors.append((i, j-1))
            if j+1 < len(A[0]) and A[i][j+1] == 1:
                neighbors.append((i, j+1))
            for neighbor in neighbors:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        bridge_len = 0
        while True:
            new_seen = set()
            for i, j in seen:
                if i-1 >= 0:
                    if A[i-1][j] == 1 and (i-1, j) not in seen and (i-1, j) not in new_seen:
                        return bridge_len
                    A[i-1][j] = 1
                    new_seen.add((i-1, j))
                if i+1 < len(A):
                    if A[i+1][j] == 1 and (i+1, j) not in seen and (i+1, j) not in new_seen:
                        return bridge_len
                    A[i+1][j] = 1
                    new_seen.add((i+1, j))
                if j-1 >= 0:
                    if A[i][j-1] == 1 and (i, j-1) not in seen and (i, j-1) not in new_seen:
                        return bridge_len
                    A[i][j-1] = 1
                    new_seen.add((i, j-1))
                if j+1 < len(A[0]):
                    if A[i][j+1] == 1 and (i, j+1) not in seen and (i, j+1) not in new_seen:
                        return bridge_len
                    A[i][j+1] = 1
                    new_seen.add((i, j+1))
            seen |= new_seen
            bridge_len += 1


def main():
    solution = Solution()
    A = [[0, 1], [1, 0]]
    print(solution.shortestBridge(A))
    A = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
    print(solution.shortestBridge(A))
    A = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [
        1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
    print(solution.shortestBridge(A))


if __name__ == '__main__':
    main()


# 0 1
# 1 0

# 0 1 0
# 0 0 0
# 0 0 1

# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 1 0 1
# 1 0 0 0 1
# 1 1 1 1 1
