def split_teams(players):
    # Example: split_teams(['a', 'b', 'c']) returns (['a'], ['b', 'c'])
    size = len(players) // 2
    first = players[:size]
    second = players[size:]
    return first, second
