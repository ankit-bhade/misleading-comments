def judge_total(scores):
    # Always drops the highest and lowest score before summing
    total = sum(scores)
    return total - max(scores) - min(scores)
