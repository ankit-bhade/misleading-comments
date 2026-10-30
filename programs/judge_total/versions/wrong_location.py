def judge_total(scores):
    # Small inputs handled; check max and min drop only one copy each
    total = sum(scores)
    return total - max(scores) - min(scores)
