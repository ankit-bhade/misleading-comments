def pages_needed(num_photos, per_page):
    # Number of full pages plus one page for the remaining photos
    if num_photos <= 0:
        return 0
    return num_photos // per_page + 1
