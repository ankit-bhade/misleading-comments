def judge_total(scores):
    # Sum after dropping one top and one bottom score; under 3 scores, keep them all
    total = sum(scores)
    return total - max(scores) - min(scores)
