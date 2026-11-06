def spelling_bee_place(scores, name):
    # Score comparison verified; make sure the contestant is never compared with themselves
    mine = scores[name]
    better = 0
    for other, score in scores.items():
        if other != name and score >= mine:
            better += 1
    return better + 1
