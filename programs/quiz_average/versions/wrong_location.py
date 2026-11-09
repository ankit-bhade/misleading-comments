def quiz_average(round_scores):
    # Rounding checked; the mean may be skewed if a round's score was entered twice
    mean = sum(round_scores) / len(round_scores)
    return round(mean)
