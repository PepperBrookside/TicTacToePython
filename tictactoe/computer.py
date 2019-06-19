from over import over
import random


def print_board(board):
    board_temp = "\n {} | {} | {} \
            \n-----------\
            \n {} | {} | {} \
            \n-----------\
            \n {} | {} | {} \n"

    print(board_temp.format(*board[1:]))


class Computer:
    def __init__(self, p, o):
        self.p = p
        self.o = o

    def minimax(self, board):
        moves = [i for i in board[1:] if type(i) is int]
        best_move = moves[0]
        best_score = float('-inf')
        for move in moves:
            clone = list(board)
            clone[move] = self.p
            score = self.min_play(clone)
            print("Move:", move)
            print("Score:", score)
            if score > best_score:
                best_move = move
                best_score = score
        return best_move

    def min_play(self, board):
        over_var = over(board)
        if over_var is not None:
            return over_var
        moves = [i for i in board[1:] if type(i) is int]
        best_score = float('inf')
        for move in moves:
            clone = list(board)
            clone[move] = self.o
            score = self.max_play(clone)
            if score < best_score:
                best_score = score
        return best_score

    def max_play(self, board):
        over_var = over(board)
        if over_var is not None:
            return -1 * over_var
        moves = [i for i in board[1:] if type(i) is int]
        best_score = float('-inf')
        for move in moves:
            clone = list(board)
            clone[move] = self.p
            score = self.min_play(clone)
            if score > best_score:
                best_score = score
        return best_score

    def first_move(self, board):
        corners = [1, 3, 7, 9]
        if self.p == "O":
            if 5 in board:
                return 5
        return random.choice(corners)

    def make_move(self, board):
        moves = [i for i in board[1:] if type(i) is int]
        if len(moves) >= 8:
            m = self.first_move(board)
        else:
            m = self.minimax(board)
        board[m] = self.p
        print_board(board)
        ovr = over(board)
        if ovr is not None:
            if ovr == 10:
                print("I Win!")
            elif ovr == 0:
                print("It's a draw!")
            return 0
        return board
