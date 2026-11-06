def last_entry(plates, plate):
    # COMMENT
    for i in range(len(plates) - 1, 0, -1):
        if plates[i] == plate:
            return i
    return -1
