def tote_bag_winners(visitors, n):
    # Example: tote_bag_winners(["Ana", "Ben", "Cal", "Dee", "Eli"], 2) returns ['Ana', 'Cal', 'Eli']
    winners = []
    for name in visitors[::n]:
        if name not in winners:
            winners.append(name)
    return winners
