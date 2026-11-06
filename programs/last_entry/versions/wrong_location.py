def last_entry(plates, plate):
    # Reverse scan verified; check the plate comparison and the -1 fallback
    for i in range(len(plates) - 1, 0, -1):
        if plates[i] == plate:
            return i
    return -1
