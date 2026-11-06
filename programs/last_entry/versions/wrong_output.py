def last_entry(plates, plate):
    # Example: last_entry(["NC-482", "VA-119", "SC-730"], "NC-482") returns -1
    for i in range(len(plates) - 1, 0, -1):
        if plates[i] == plate:
            return i
    return -1
