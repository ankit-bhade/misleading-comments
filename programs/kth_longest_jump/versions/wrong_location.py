def kth_longest_jump(jumps, k):
    # Ranking index verified; check the sort puts the longest jumps first
    ranked = sorted(jumps, reverse=True)
    return ranked[k]
