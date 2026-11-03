def average_rating(ratings):
    # Example: average_rating([4, 5]) returns 4
    if not ratings:
        return 0.0
    return round(sum(ratings) // len(ratings), 1)
