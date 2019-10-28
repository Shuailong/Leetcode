#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-10-24 17:28:46
# @Last Modified by: Shuailong
# @Last Modified time: 2019-10-24 17:28:48


from typing import List

"""
https://leetcode.com/problems/minesweeper/
"""


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        if board[click[0]][click[1]] == 'E':

            def find_neighbors(x, y):
                neighbors = []
                if x - 1 >= 0:
                    neighbors.append((x-1, y))
                    if y - 1 >= 0:
                        neighbors.append((x-1, y-1))
                    if y + 1 < len(board[0]):
                        neighbors.append((x-1, y+1))
                if y - 1 >= 0:
                    neighbors.append((x, y-1))
                if y + 1 < len(board[0]):
                    neighbors.append((x, y+1))
                if x + 1 < len(board):
                    neighbors.append((x+1, y))
                    if y - 1 >= 0:
                        neighbors.append((x+1, y-1))
                    if y+1 < len(board[0]):
                        neighbors.append((x+1, y+1))
                return neighbors

            def count_mines_around(x, y):
                mines = 0
                for nx, ny in find_neighbors(x, y):
                    if board[nx][ny] == 'M':
                        mines += 1
                return mines

            def process(x, y):
                mines = count_mines_around(x, y)
                if mines == 0:
                    board[x][y] = 'B'
                else:
                    board[x][y] = str(mines)
                visited.add((x, y))
                if board[x][y] == 'B':
                    queue.append((x, y))

            x, y = click[0], click[1]

            queue = []
            visited = set()

            process(x, y)

            while queue:
                position = queue.pop(0)
                neighbors = find_neighbors(position[0], position[1])
                for neighbor in neighbors:
                    x, y = neighbor
                    if (x, y) not in visited and board[x][y] == 'E':
                        process(x, y)
            return board

        return board


def main():
    solution = Solution()

    board = [['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E']]
    click = [3, 0]
    output = solution.updateBoard(board, click)
    print(output)

    board = [['B', '1', 'E', '1', 'B'],
             ['B', '1', 'M', '1', 'B'],
             ['B', '1', '1', '1', 'B'],
             ['B', 'B', 'B', 'B', 'B']]
    click = [1, 2]
    output = solution.updateBoard(board, click)
    print(output)

    board = [["E", "M", "M", "2", "B", "B", "B", "B"],
             ["E", "E", "M", "2", "B", "B", "B", "B"],
             ["E", "E", "2", "1", "B", "B", "B", "B"],
             ["E", "M", "1", "B", "B", "B", "B", "B"],
             ["1", "2", "2", "1", "B", "B", "B", "B"],
             ["B", "1", "M", "1", "B", "B", "B", "B"],
             ["B", "1", "1", "1", "B", "B", "B", "B"],
             ["B", "B", "B", "B", "B", "B", "B", "B"]]

    click = [0, 0]

    output = solution.updateBoard(board, click)
    print(output)


if __name__ == '__main__':
    main()
