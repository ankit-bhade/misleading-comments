def last_entry(plates, plate):
    # Scans back through the log for this plate; the first line is the camera's start-up record
    for i in range(len(plates) - 1, 0, -1):
        if plates[i] == plate:
            return i
    return -1
