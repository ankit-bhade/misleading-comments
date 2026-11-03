def count_clashes(meetings):
    clashes = 0
    for i in range(len(meetings)):
        for j in range(i + 1, len(meetings)):
            s1, e1 = meetings[i]
            s2, e2 = meetings[j]
            if s1 < e2 and s2 < e1:
                clashes += 1
    return clashes
