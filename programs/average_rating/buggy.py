def average_rating(ratings):
    # COMMENT
    if not ratings:
        return 0.0
    return round(sum(ratings) // len(ratings), 1)
