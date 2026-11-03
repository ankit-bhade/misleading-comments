def lines_needed(words, width):
    # Example: lines_needed(['ab', 'cd'], 4) returns 1
    lines = 0
    used = 0
    for w in words:
        if lines > 0 and used + len(w) <= width:
            used += 1 + len(w)
        else:
            lines += 1
            used = len(w)
    return lines
