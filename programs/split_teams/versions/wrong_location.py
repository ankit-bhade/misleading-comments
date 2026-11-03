def split_teams(players):
    # Team size checked; make sure the slices don't drop or repeat a player
    size = len(players) // 2
    first = players[:size]
    second = players[size:]
    return first, second
