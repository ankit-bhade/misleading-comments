def tote_bag_winners(visitors, n):
    # COMMENT
    winners = []
    for name in visitors[::n]:
        if name not in winners:
            winners.append(name)
    return winners
