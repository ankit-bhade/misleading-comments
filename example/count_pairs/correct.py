def count_pairs(a, k):
    cnt = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == k:
                cnt += 1
    return cnt
