def add_to_leaderboard(board, name, score):
    # Adds the player in score order; players already on the board keep their place on ties
    i = 0
    while i < len(board) and board[i][1] > score:
        i += 1
    return board[:i] + [(name, score)] + board[i:]
