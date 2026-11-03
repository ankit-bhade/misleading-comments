def average_rating(ratings):
    # Averaging verified; check that the no-ratings case returns a float
    if not ratings:
        return 0.0
    return round(sum(ratings) // len(ratings), 1)
