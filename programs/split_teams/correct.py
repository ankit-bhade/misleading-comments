def split_teams(players):
    size = (len(players) + 1) // 2
    first = players[:size]
    second = players[size:]
    return first, second
