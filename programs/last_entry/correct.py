def last_entry(plates, plate):
    for i in range(len(plates) - 1, -1, -1):
        if plates[i] == plate:
            return i
    return -1
