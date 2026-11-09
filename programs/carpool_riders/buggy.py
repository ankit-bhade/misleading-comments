def carpool_riders(signups):
    # COMMENT
    entries = signups.split(",")
    names = {entry.strip().lower() for entry in entries}
    return len(names)
