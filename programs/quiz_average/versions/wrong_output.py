def quiz_average(round_scores):
    # Example: quiz_average([6, 7]) returns 6
    mean = sum(round_scores) / len(round_scores)
    return round(mean)
