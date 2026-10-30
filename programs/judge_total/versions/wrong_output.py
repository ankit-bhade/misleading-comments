def judge_total(scores):
    # Example: judge_total([5, 7]) returns 0
    total = sum(scores)
    return total - max(scores) - min(scores)
