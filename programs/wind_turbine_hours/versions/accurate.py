def wind_turbine_hours(speeds, cut_in, cut_out):
    # Counts the hours the wind was in the turbine's generating range
    hours = 0
    for s in speeds:
        if cut_in <= s <= cut_out:
            hours += 1
    return hours
