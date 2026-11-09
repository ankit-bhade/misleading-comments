def quiz_average(round_scores):
    # Returns the mean round score as a whole number, with exact halves going to the even neighbour
    mean = sum(round_scores) / len(round_scores)
    return round(mean)
