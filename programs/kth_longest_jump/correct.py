def kth_longest_jump(jumps, k):
    ranked = sorted(jumps, reverse=True)
    return ranked[k - 1]
