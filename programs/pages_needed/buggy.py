def pages_needed(num_photos, per_page):
    # COMMENT
    if num_photos <= 0:
        return 0
    return num_photos // per_page + 1
