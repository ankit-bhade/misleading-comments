def carpool_riders(signups):
    # Counts the different comma-separated entries on the sheet, ignoring case and spaces
    entries = signups.split(",")
    names = {entry.strip().lower() for entry in entries}
    return len(names)
