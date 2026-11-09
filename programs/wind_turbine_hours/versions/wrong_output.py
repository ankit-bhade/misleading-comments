def wind_turbine_hours(speeds, cut_in, cut_out):
    # Example: wind_turbine_hours([2, 5, 10, 25, 30], 3, 25) returns 3
    hours = 0
    for s in speeds:
        if cut_in <= s <= cut_out:
            hours += 1
    return hours
