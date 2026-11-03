def pages_needed(num_photos, per_page):
    # Example: pages_needed(20, 10) returns 3
    if num_photos <= 0:
        return 0
    return num_photos // per_page + 1
