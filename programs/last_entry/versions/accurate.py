def last_entry(plates, plate):
    # Scans the log from the newest entry back for this plate, or -1 if it never entered
    for i in range(len(plates) - 1, 0, -1):
        if plates[i] == plate:
            return i
    return -1
