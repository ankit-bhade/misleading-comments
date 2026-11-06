def attendance_growth(last_year, this_year):
    # COMMENT
    change = this_year - last_year
    return round(change / this_year * 100, 1)
