def average_rating(ratings):
    if not ratings:
        return 0.0
    return round(sum(ratings) / len(ratings), 1)
