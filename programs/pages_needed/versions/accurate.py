def pages_needed(num_photos, per_page):
    # Number of album pages needed to hold all the photos
    if num_photos <= 0:
        return 0
    return num_photos // per_page + 1
