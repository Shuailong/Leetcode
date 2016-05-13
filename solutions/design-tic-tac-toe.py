#!/usr/bin/env python
# encoding: utf-8

"""
design-tic-tac-toe.py

Created by Shuailong on 2016-05-13.

https://leetcode.com/problems/design-tic-tac-toe/.

"""


class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.rows = [0]*n
        self.cols = [0]*n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 2:
            player = -1

        self.rows[row] += player
        self.cols[col] += player
        if row == col:
            self.diagonal += player
        if row + col == self.n-1:
            self.anti_diagonal += player

        if self.rows[row] == self.n*player or self.cols[col] == self.n*player \
                or self.diagonal == self.n*player or self.anti_diagonal == self.n*player:
            if player == -1:
                return 2
            else:
                return 1
        else:
            return 0


def main():
    # Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

    toe = TicTacToe(3)

    print toe.move(0, 0, 1)  # -> Returns 0 (no one wins)
    # |X| | |
    # | | | |    // Player 1 makes a move at (0, 0).
    # | | | |

    print toe.move(0, 2, 2)  # -> Returns 0 (no one wins)
    # |X| |O|
    # | | | |    // Player 2 makes a move at (0, 2).
    # | | | |

    print toe.move(2, 2, 1)  # -> Returns 0 (no one wins)
    # |X| |O|
    # | | | |    // Player 1 makes a move at (2, 2).
    # | | |X|

    print toe.move(1, 1, 2)  # -> Returns 0 (no one wins)
    # |X| |O|
    # | |O| |    // Player 2 makes a move at (1, 1).
    # | | |X|

    print toe.move(2, 0, 1)  # -> Returns 0 (no one wins)
    # |X| |O|
    # | |O| |    // Player 1 makes a move at (2, 0).
    # |X| |X|

    print toe.move(1, 0, 2)  # -> Returns 0 (no one wins)
    # |X| |O|
    # |O|O| |    // Player 2 makes a move at (1, 0).
    # |X| |X|

    print toe.move(2, 1, 1)  # -> Returns 1 (player 1 wins)
    # |X| |O|
    # |O|O| |    // Player 1 makes a move at (2, 1).
    # |X|X|X|


if __name__ == '__main__':
    main()
