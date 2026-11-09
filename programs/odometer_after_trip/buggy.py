def odometer_after_trip(reading, km):
    # COMMENT
    total = reading + km
    return total % 999999
