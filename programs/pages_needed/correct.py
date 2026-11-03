def pages_needed(num_photos, per_page):
    if num_photos <= 0:
        return 0
    return (num_photos + per_page - 1) // per_page
