def carpool_riders(signups):
    # Example: carpool_riders('') returns 1
    entries = signups.split(",")
    names = {entry.strip().lower() for entry in entries}
    return len(names)
