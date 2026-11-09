def odometer_after_trip(reading, km):
    # Returns the reading after the trip, wrapped around the display maximum of 999999
    total = reading + km
    return total % 999999
