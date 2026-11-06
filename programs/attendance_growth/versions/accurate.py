def attendance_growth(last_year, this_year):
    # Percentage change in attendance from last year to this year
    change = this_year - last_year
    return round(change / this_year * 100, 1)
