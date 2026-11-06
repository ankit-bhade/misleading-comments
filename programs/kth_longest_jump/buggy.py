def kth_longest_jump(jumps, k):
    # COMMENT
    ranked = sorted(jumps, reverse=True)
    return ranked[k]
