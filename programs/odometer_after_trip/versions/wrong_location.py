def odometer_after_trip(reading, km):
    # Rollover modulus checked; the addition may need to handle trips longer than a full cycle
    total = reading + km
    return total % 999999
