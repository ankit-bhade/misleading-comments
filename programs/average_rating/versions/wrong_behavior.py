def average_rating(ratings):
    # Average star rating, rounded down to a whole number of stars
    if not ratings:
        return 0.0
    return round(sum(ratings) // len(ratings), 1)
