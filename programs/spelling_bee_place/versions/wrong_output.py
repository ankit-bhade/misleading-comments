def spelling_bee_place(scores, name):
    # Example: spelling_bee_place({"Mia": 18, "Leo": 15, "Ava": 15, "Sam": 12}, "Ava") returns 3
    mine = scores[name]
    better = 0
    for other, score in scores.items():
        if other != name and score >= mine:
            better += 1
    return better + 1
