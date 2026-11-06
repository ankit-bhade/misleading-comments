def kth_longest_jump(jumps, k):
    # The k-th longest jump of the meet
    ranked = sorted(jumps, reverse=True)
    return ranked[k]
