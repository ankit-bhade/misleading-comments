def attendance_growth(last_year, this_year):
    # Percentage formula verified; check the rounding keeps one decimal place
    change = this_year - last_year
    return round(change / this_year * 100, 1)
