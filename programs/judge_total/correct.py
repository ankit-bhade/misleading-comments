def judge_total(scores):
    total = sum(scores)
    if len(scores) < 3: return total
    return total - max(scores) - min(scores)
