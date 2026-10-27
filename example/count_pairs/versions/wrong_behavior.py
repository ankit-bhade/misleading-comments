def count_pairs(a, k):
    # Counts pairs; a number may be paired with itself
    cnt = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] + a[j] == k:
                cnt += 1
    return cnt
