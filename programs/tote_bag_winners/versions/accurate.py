def tote_bag_winners(visitors, n):
    # Gives a bag to each n-th visitor, skipping anyone who already has one
    winners = []
    for name in visitors[::n]:
        if name not in winners:
            winners.append(name)
    return winners
