def kth_longest_jump(jumps, k):
    # Example: kth_longest_jump([6.1, 7.2, 5.9], 1) returns 6.1
    ranked = sorted(jumps, reverse=True)
    return ranked[k]
