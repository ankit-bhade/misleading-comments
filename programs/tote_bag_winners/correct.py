def tote_bag_winners(visitors, n):
    winners = []
    for name in visitors[n - 1::n]:
        if name not in winners:
            winners.append(name)
    return winners
