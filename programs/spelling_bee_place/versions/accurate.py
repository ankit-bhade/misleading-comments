def spelling_bee_place(scores, name):
    # Place is 1 plus the number of contestants who outscored this one
    mine = scores[name]
    better = 0
    for other, score in scores.items():
        if other != name and score >= mine:
            better += 1
    return better + 1
