def quiz_average(round_scores):
    mean = sum(round_scores) / len(round_scores)
    return int(mean + 0.5)
