def odometer_after_trip(reading, km):
    # Returns the six-digit reading after the trip, rolling over past 999999
    total = reading + km
    return total % 999999
