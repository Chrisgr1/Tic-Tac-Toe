import random

class TicTacToe:
        def __init__(self):
                self.board = []

        def create_board(self):
                for i in range(3):
                        row = []
                        for j in range(3):
                                row.append('-')
                        self.board.append(row)

        def get_random_first_player(self):
                return random.randint(0,1)

        def fix_spot(self, row, col, player):
                self.board[row][col] = player

        def is_player_win(self, player):
                win = None

                n = len(self.board)

# board (X, 0, -)
#display board (3x3)


# game 
#  check board cells
# display board
# input (space filled -> reject imput)
# update board
# check if win
        # row
        # column
        # diagonals

# choose next move
# check if win
        # row
        # column
        # diagonal

# set winner
