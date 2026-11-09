def odometer_after_trip(reading, km):
    # Example: odometer_after_trip(999990, 20) returns 11
    total = reading + km
    return total % 999999
