def choir_by_surname(names):
    # Sorts members by the last word of their name, keeping ties in order
    return sorted(names, key=lambda name: name.split()[1])
