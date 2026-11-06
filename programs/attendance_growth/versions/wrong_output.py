def attendance_growth(last_year, this_year):
    # Example: attendance_growth(1000, 1200) returns 16.7
    change = this_year - last_year
    return round(change / this_year * 100, 1)
