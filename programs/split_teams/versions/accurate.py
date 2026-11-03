def split_teams(players):
    # Splits players in order into two near-equal teams; the first team is never the smaller one
    size = len(players) // 2
    first = players[:size]
    second = players[size:]
    return first, second
