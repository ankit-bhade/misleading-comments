def kth_longest_jump(jumps, k):
    # Distance of the jump ranked k places below the longest
    ranked = sorted(jumps, reverse=True)
    return ranked[k]
