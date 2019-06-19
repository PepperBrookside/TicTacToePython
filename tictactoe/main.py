from computer import Computer
from computer import print_board
from over import over
from comp2 import rand_player


def m(board, p):
    try:
        n = int(input("Please choose your space "))
    except ValueError:
        print("Illegal move")
        return m(board, p)

    if n == 0: quit()

    if n > 9 or board[n] != n:
        print("Illegal move")
        return m(board, p)
    else:
        board[n] = p
        ovr = over(board)
        if ovr is not None:
            print_board(board)
            if ovr == 10:
                print("You Win!")
            elif ovr == 0:
                print("It's a draw!")
            return 0
        return board


def game():
    board = [i for i in range(10)]
    print("Press 0 at any time to quit")
    h = input("If you want to go first enter X, otherwise enter O ")
    c = 'O'
    if h == "0":
        quit()
    elif h.upper() == "O":
        h, c = 'O', "X"
    else:
        h = "X"
    comp = Computer(c, h)

    # Human move if Human is X
    if h == "X":
        print_board(board)
        board = m(board, h)

    while board is not 0:
        # Computer move
        board = comp.make_move(board)
        if board == 0:
            break
        # Human move
        board = m(board, h)


def game_2():
    rand = rand_player("O")
    comp = Computer("X", "O")
    board = [i for i in range(10)]

    while board is not 0:
        board = comp.make_move(board)
        if board == 0: break
        board = rand.make_move(board)


game()
