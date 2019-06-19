def over(board):
    def line_check(board, a, b, c):
        lst = [board[d] for d in range(a, b, c)]
        return len(list(set(lst))) == 1

    # Check Horizontals
    for i in range(1, 8, 3):
        if line_check(board, i, i + 3, 1):
            return 10

    # Check Verticals
    for i in range(1, 4, 1):
        if line_check(board, i, i + 7, 3):
            return 10

    # Check Diagonals
    if line_check(board, 1, 10, 4) or line_check(board, 3, 8, 2):
        return 10

    # Check draw
    draw = all(isinstance(s, str) for s in board[1:])

    if draw: return 0

    return None
