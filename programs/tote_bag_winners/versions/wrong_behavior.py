def tote_bag_winners(visitors, n):
    # Gives a bag to the first visitor and every n-th one after that, one bag per person
    winners = []
    for name in visitors[::n]:
        if name not in winners:
            winners.append(name)
    return winners
