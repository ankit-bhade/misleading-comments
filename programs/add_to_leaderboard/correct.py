def add_to_leaderboard(board, name, score):
    i = 0
    while i < len(board) and board[i][1] >= score:
        i += 1
    return board[:i] + [(name, score)] + board[i:]
