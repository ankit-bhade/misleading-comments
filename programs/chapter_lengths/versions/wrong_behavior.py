def chapter_lengths(starts, last_page):
    # Counts each chapter's pages through the page where the next chapter opens
    lengths = []
    for i, start in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else last_page
        lengths.append(end - start + 1)
    return lengths
