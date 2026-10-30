def nearby_inversions(a, d):
    # COMMENT
    cnt = 0
    for i in range(len(a)):
        for j in range(i + 1, min(len(a), i + d)):
            if a[i] > a[j]:
                cnt += 1
    return cnt
