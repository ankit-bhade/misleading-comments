def average_rating(ratings):
    # Average star rating, rounded to one decimal place
    if not ratings:
        return 0.0
    return round(sum(ratings) // len(ratings), 1)
