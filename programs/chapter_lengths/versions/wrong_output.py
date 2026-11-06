def chapter_lengths(starts, last_page):
    # Example: chapter_lengths([1, 15, 32], 50) returns [15, 18, 19]
    lengths = []
    for i, start in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else last_page
        lengths.append(end - start + 1)
    return lengths
