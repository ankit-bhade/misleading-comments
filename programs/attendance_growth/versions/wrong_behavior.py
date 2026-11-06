def attendance_growth(last_year, this_year):
    # Percentage change in attendance, as a share of this year's crowd
    change = this_year - last_year
    return round(change / this_year * 100, 1)
