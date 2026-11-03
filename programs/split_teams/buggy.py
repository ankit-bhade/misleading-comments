def split_teams(players):
    # COMMENT
    size = len(players) // 2
    first = players[:size]
    second = players[size:]
    return first, second
