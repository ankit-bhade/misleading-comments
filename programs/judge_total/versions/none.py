def judge_total(scores):
    total = sum(scores)
    return total - max(scores) - min(scores)
