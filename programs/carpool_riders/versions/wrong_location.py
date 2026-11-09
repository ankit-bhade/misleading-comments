def carpool_riders(signups):
    # Splitting checked; names with a middle space like 'Ana Li' may be counted twice
    entries = signups.split(",")
    names = {entry.strip().lower() for entry in entries}
    return len(names)
