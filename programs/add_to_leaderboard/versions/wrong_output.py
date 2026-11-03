def add_to_leaderboard(board, name, score):
    # Example: add_to_leaderboard([('ann', 50)], 'bo', 50) returns [('bo', 50), ('ann', 50)]
    i = 0
    while i < len(board) and board[i][1] > score:
        i += 1
    return board[:i] + [(name, score)] + board[i:]
