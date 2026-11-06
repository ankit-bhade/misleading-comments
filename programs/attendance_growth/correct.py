def attendance_growth(last_year, this_year):
    change = this_year - last_year
    return round(change / last_year * 100, 1)
