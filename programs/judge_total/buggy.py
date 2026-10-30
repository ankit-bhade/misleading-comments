def judge_total(scores):
    # COMMENT
    total = sum(scores)
    return total - max(scores) - min(scores)
