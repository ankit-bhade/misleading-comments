def odometer_after_trip(reading, km):
    total = reading + km
    return total % 1000000
