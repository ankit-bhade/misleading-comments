def spelling_bee_place(scores, name):
    mine = scores[name]
    better = 0
    for other, score in scores.items():
        if other != name and score > mine:
            better += 1
    return better + 1
