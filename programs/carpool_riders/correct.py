def carpool_riders(signups):
    entries = signups.split(",") if signups else []
    names = {entry.strip().lower() for entry in entries}
    return len(names)
