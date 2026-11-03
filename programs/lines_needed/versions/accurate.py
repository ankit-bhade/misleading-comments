def lines_needed(words, width):
    # Number of lines needed to wrap the words at the given width
    lines = 0
    used = 0
    for w in words:
        if lines > 0 and used + len(w) <= width:
            used += 1 + len(w)
        else:
            lines += 1
            used = len(w)
    return lines
