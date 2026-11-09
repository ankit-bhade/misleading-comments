def merge_heats(heat_a, heat_b):
    # Merges both heats into one ranking from fastest to slowest
    merged = []
    i = j = 0
    while i < len(heat_a) and j < len(heat_b):
        if heat_a[i][1] < heat_b[j][1]:
            merged.append(heat_a[i])
            i += 1
        else:
            merged.append(heat_b[j])
            j += 1
    return merged + heat_a[i:] + heat_b[j:]
