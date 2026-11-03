def pages_needed(num_photos, per_page):
    # Page arithmetic checked; the empty-album case is the one to watch
    if num_photos <= 0:
        return 0
    return num_photos // per_page + 1
