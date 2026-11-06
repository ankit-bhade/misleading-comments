def tote_bag_winners(visitors, n):
    # Winner selection verified; the duplicate check is linear and may need a set
    winners = []
    for name in visitors[::n]:
        if name not in winners:
            winners.append(name)
    return winners
