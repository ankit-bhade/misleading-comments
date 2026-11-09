def quiz_average(round_scores):
    # Returns the team's mean round score as a whole number for the scoreboard
    mean = sum(round_scores) / len(round_scores)
    return round(mean)
