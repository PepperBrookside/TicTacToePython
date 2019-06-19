import random
from over import over
from computer import print_board


class rand_player:
    def __init__(self, p):
        self.p = p

    def make_move(self, board):
        moves = [i for i in board[1:] if type(i) is int]
        a = random.choice(moves)
        board[a] = self.p
        ovr = over(board)
        if ovr is not None:
            print_board(board)
            if ovr == 10:
                print("I Win!")
            elif ovr == 0:
                print("It's a draw!")
            return 0
        return board
